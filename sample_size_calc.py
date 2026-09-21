"""
표본크기/검정력 계산 — KIST-JBNU 다중 바이오센서 카트리지 검증 프로토콜
근거: Cohen (1988), power=0.80, alpha=0.05, 양측검정
"""
import numpy as np
from scipy import stats

Z_ALPHA = stats.norm.ppf(1 - 0.05 / 2)  # 1.959964
Z_BETA = stats.norm.ppf(0.80)           # 0.841621

print(f"Z_alpha/2 (two-tailed, 0.05) = {Z_ALPHA:.4f}")
print(f"Z_beta (power=0.80)         = {Z_BETA:.4f}")

# ---------------------------------------------------------------
# 1. 코펩틴 단독 vs 코펩틴+S100b 병합 패널 — McNemar discordant-pair 기반
#    출처: Deboevere et al. 2019, Scand J Trauma Resusc Emerg Med
#    (DOI 10.1186/s13049-019-0651-1), N=135 (stroke 13, non-stroke 122)
#    컷오프: 코펩틴 >10 pmol/L, PS100 >0.105 μmol/L. 병합 규칙 = 둘 중 하나라도 양성(OR).
#    코펩틴 단독 10/13 양성(76.9%, 논문 반올림 표기 77%), 병합 13/13(100%).
#    OR 규칙 구조상 c(코펩틴+, 병합-)=0은 항상 성립(코펩틴 양성이면 병합도 자동 양성).
#    b(코펩틴-, 병합+)=3은 논문 원문 sens 수치(10/13 -> 13/13)에서 직접 역산되는 값
#    (=S100b 단독 양성으로 병합 판정에 편입된 stroke 환자 수), 가정이 아닌 확정값.
# ---------------------------------------------------------------
print("\n=== 1. 코펩틴 단독 vs 코펩틴+S100b 병합 (stroke 확진군 대상) ===")

n_stroke_pilot = 13
b_plus_c_pilot = 3
discordant_rate_pilot = b_plus_c_pilot / n_stroke_pilot
print(f"파일럿 discordant rate = {b_plus_c_pilot}/{n_stroke_pilot} = {discordant_rate_pilot:.3f}")

# 파일럿 관측치(3/3 100%)는 소표본 극단값이므로, 계획값은 보수적으로 하향(85%)
p0 = 0.50  # H0: 대칭(개선 없음)
p1_conservative = 0.85  # 계획 가정: discordant pair의 85%가 병합 패널 유리

def one_sample_prop_n(p0, p1, z_alpha=Z_ALPHA, z_beta=Z_BETA):
    num = z_alpha * np.sqrt(p0 * (1 - p0)) + z_beta * np.sqrt(p1 * (1 - p1))
    return (num / (p1 - p0)) ** 2

n_discordant_needed = one_sample_prop_n(p0, p1_conservative)
n_stroke_needed = n_discordant_needed / discordant_rate_pilot

print(f"필요 discordant pair 수 (p1={p1_conservative}) = {n_discordant_needed:.1f} -> 올림 {np.ceil(n_discordant_needed):.0f}")
print(f"필요 stroke 확진 표본수 = {n_discordant_needed:.1f} / {discordant_rate_pilot:.3f} = {n_stroke_needed:.1f} -> 올림 {np.ceil(n_stroke_needed):.0f}명")

# 월 stroke 확진 AVS 환자 수 추정: 월 AVS 20~30명 중 파일럿 stroke 비율 10%(13/135) 적용
avs_per_month_low, avs_per_month_high = 20, 30
stroke_rate_pilot = 13 / 135
stroke_per_month_low = avs_per_month_low * stroke_rate_pilot
stroke_per_month_high = avs_per_month_high * stroke_rate_pilot
print(f"파일럿 stroke 비율 = 13/135 = {stroke_rate_pilot:.3f}")
print(f"월 stroke 확진 AVS 예상 환자수 = {stroke_per_month_low:.1f}~{stroke_per_month_high:.1f}명")

months_low = np.ceil(n_stroke_needed) / stroke_per_month_high
months_high = np.ceil(n_stroke_needed) / stroke_per_month_low
print(f"목표 도달 예상 기간 = {months_low:.1f}~{months_high:.1f}개월")

# ---------------------------------------------------------------
# 2. CGRP (타액, interictal 편두통 vs 대조군)
#    Alpuente et al. 2022, Cephalalgia 42(3):186-196 (DOI 10.1177/03331024211040467)
#    -- 2020 medRxiv preprint(10.1101/2020.11.18.20233841)의 정식 출판본. 대조군 n과 수치가
#       preprint(13명, median 42.2)에서 출판본(22명, median 54.3)으로 변경됨 -- 출판본 값을 사용.
#    환자 22명 median 98.0 IQR 80.3 / 대조군 22명 median 54.3 IQR 44.0, p=0.034
#    median/IQR -> SD 근사: Wan et al. 2014 (BMC Med Res Methodol), SD ~= IQR / 1.35
# ---------------------------------------------------------------
print("\n=== 2. 타액 CGRP: interictal 편두통 vs 대조군 (출판본 수치) ===")

n_pt, iqr_pt, med_pt = 22, 80.3, 98.0
n_hc, iqr_hc, med_hc = 22, 44.0, 54.3

sd_pt = iqr_pt / 1.35
sd_hc = iqr_hc / 1.35
pooled_sd = np.sqrt(((n_pt - 1) * sd_pt**2 + (n_hc - 1) * sd_hc**2) / (n_pt + n_hc - 2))
cohens_d = (med_pt - med_hc) / pooled_sd

print(f"SD 근사(환자) = {iqr_pt}/1.35 = {sd_pt:.2f}")
print(f"SD 근사(대조군) = {iqr_hc}/1.35 = {sd_hc:.2f}")
print(f"Pooled SD = {pooled_sd:.2f}")
print(f"Cohen's d = {cohens_d:.3f}")

def two_sample_n_per_group(d, z_alpha=Z_ALPHA, z_beta=Z_BETA):
    return 2 * ((z_alpha + z_beta) / d) ** 2

n_per_group = two_sample_n_per_group(cohens_d)
print(f"군당 필요 표본수 = {n_per_group:.1f} -> 올림 {np.ceil(n_per_group):.0f}명")

# ---------------------------------------------------------------
# 3. 코펩틴 단독의 단독 사용 정밀도(참고): 관측 sens=77%(10/13)의 Wilson 95% CI
# ---------------------------------------------------------------
print("\n=== 참고: 코펩틴 단독 민감도 파일럿 CI (Wilson score) ===")
from statsmodels.stats.proportion import proportion_confint
ci_low, ci_high = proportion_confint(10, 13, alpha=0.05, method='wilson')
print(f"n=13, 10/13 -> Wilson 95% CI = [{ci_low:.3f}, {ci_high:.3f}]")
