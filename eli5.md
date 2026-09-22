---
layout: page
title: 20260922
permalink: /eli5/
---

<script>
  window.MathJax = {
    tex: {
      inlineMath: [['$', '$'], ['\\(', '\\)']]
    }
  };
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.js" id="MathJax-script" async></script>

## KIST-JBNU 바이오센서 마커

KIST와 전북대병원은 
- 혈액·침·눈물 카트리지 센서 개발과
- 안구운동 AI 분석(Eye-ECG)을 함께 논의 중이다.

바이오센서 카트리지 쪽은 아래 순서로 단계를 제시 해 주셨다.
**코펩틴 단일 → 코펩틴+S100B 2-plex → CGRP 안정화 → 눈물 용출 표준화**. 
이에 맞게 논문 몇 편을 가져와서 브리핑 한다.

<img width="1288" height="76" alt="image" src="https://github.com/user-attachments/assets/ab1f951c-e973-4615-b7b0-751e7558a8db" />

> 2026-08-25, 이관희 교수님 메일

이 메일 스레드를 확인 했을 때, KIST 팀이 아래 내용으로 설계를 준비 중 (제안) 이었다. 그래서 이 순서와 우선순위에 맞춰 관련 논문을 찾아 정리했고, 어떤 유의사항이 있을지 제시하고자 한다.

| 항목 | 메일 내용 |
|---|---|
| 카트리지 라인의 분리 | 표적 분자량이 substance P(1.3 kDa)부터 anti-AChR IgG(150 kDa)까지 100배 넘게 벌어져, 카트리지 하나로 묶기 어렵고 검체별·분자량대별로 나눠 병행 개발해야 할 수 있다. |
| 코펩틴+S100B 2-plex 우선순위 | 코펩틴은 실온에서 며칠 안정해 안정화 장비 없이 시작할 수 있는 유일한 표적이다. 코펩틴(조기 상승)과 S100B(지연 상승)는 시간축이 반대라, 병합 측정하면 단일 시점 측정으로도 발병 경과를 역추정할 수 있다. 1차 목표는 2-plex, LOD 각 10 pg/mL 이하, 판독 15–20분, 혈장 50 µL 이하다. |
| 메니에르/VM은 센서보다 전처리가 관건 | CGRP 반감기가 10분 남짓이라, 채혈부터 안정화까지 걸리는 시간이 결과를 좌우할 수 있다. |
| MG-Sentinel 1단계 기여 범위 조정 | 눈물 anti-AChR은 인식소자로 막단백질 AChR이 필요하고 Schirmer 용출액은 부피가 작아 난이도가 세 패널 중 가장 높다. 1단계 기여를 센서가 아니라 눈물 검체의 채취-용출-정규화 표준화로 잡자는 제안이다. |
| 연구 순서 | 코펩틴 단일 → 코펩틴+S100B 2-plex → CGRP 안정화 → 눈물 용출 표준화. 앞의 두 단계는 6개월 내 데이터가 나올 것으로 예상한다. |

---

### 코펩틴

**코펩틴**은 몸에 급한 일이 생기면 오르는 물질이다. 
- 문제는 뇌졸중이 아니어도 스트레스만 받으면 오른다는 특징이 있다는 것인데, 그렇다 보니 코펩틴 하나만 바이오마커로 사용하면 쓰면 실제 뇌졸중 환자 13명 중 3명을 놓칠 위험이 보고되었다.
(Value of copeptin and the S-100b protein assay in ruling out the diagnosis of stroke-induced dizziness pattern in emergency departments., IF 2025: 3.6)

<img width="1017" height="614" alt="image" src="https://github.com/user-attachments/assets/9af980b7-aea4-48e7-a87a-6c30d8716ffa" />

<img width="1014" height="187" alt="image" src="https://github.com/user-attachments/assets/56440930-7217-4a97-a0a6-5911b664a3e2" />

---

### S100B

**S100B**는 다르다. 뇌 조직이 실제로 손상됐을 때만 새어 나온다 (뇌척수액 등에서 나오는 것으로 wiki에서 읽었음). 
- 위와 같은 파일럿 연구에서 코펩틴과 S100B를 같이 썼더니 코펩틴이 놓친 뇌졸증 환자 3명을 S100B가 잡아냈다.
- 13명 전원을 놓치지 않았다.

<img width="1014" height="187" alt="image" src="https://github.com/user-attachments/assets/26eb927d-c702-4d15-868f-93cad158c1c8" />


---

### CGRP

**CGRP**는 로드맵 3단계("CGRP 안정화")다. 연구 논문 마다 실험 설계가 다르기도 했고, 이에 따라 결과가 다르게 보고 되었다.

#### EM의 경우
침에서 뽑아낸 CGRP가 편두통 환자 전반을 대조군과 구분하는 데 쓸모가 있다는 보고가 해외 연구에서 나온다 (Salivary CGRP can monitor the different migraine phases: CGRP (in)dependent attacks., IF 2025: 5.8) .

<img width="750" height="464" alt="image" src="https://github.com/user-attachments/assets/ffed84ac-53c9-4b69-8833-b6d8039214a7" />

<img width="748" height="491" alt="image" src="https://github.com/user-attachments/assets/6bd9faa2-4dd8-4128-b1b7-aa49dc34b644" />

---

#### 전정편두통(VM)에서는
직접 수행했던 2025년 연구(Bai, Chu, Kang, Chae, Dieterich, Oh, *Cephalalgia*)는 만성편두통(CM)·전정편두통(VM)·건강대조군(HC) 세 그룹을 함께 비교했다. 
(No change in interictal plasma and salivary CGRP levels in individuals with vestibular migraine corresponding to episodic migraine., IF 2025: 5.8)

<img width="744" height="449" alt="image" src="https://github.com/user-attachments/assets/6213ecf1-2193-454d-bf16-d8ba55cd83b8" />

이 연구는 혈장 CGRP가 CM과 VM을 가르는 데는 강하게 작동한다는 것을 보였다(AUC=0.88, CM 74.6 pg/mL vs VM 37.1 pg/mL, p<0.001). 

<img width="692" height="189" alt="image" src="https://github.com/user-attachments/assets/125faff9-49e8-40a9-bdf8-bd1e59a6d7f8" />

<img width="684" height="651" alt="image" src="https://github.com/user-attachments/assets/4b8af955-f306-450c-a6bb-2841e0368eed" />


동시에, 이번 논의 된 주제 중 하나인 **VM과 HC 사이**에서는 혈장·타액 CGRP 모두 유의한 차이가 없었다(혈장 p=1.000, 타액 p=0.699).

<img width="656" height="219" alt="image" src="https://github.com/user-attachments/assets/9efc7e7b-2505-42a3-8f36-a7ef1d4b5a67" />


즉 해당 연구에서 CGRP는 "편두통 아형을 가르는 지표"로는 유효했고 "전정편두통을 건강한 사람과 가르는 지표"로는 유효하지 않았다고 보고하고 있다.

---

#### VM-HC를 다룬 다른 연구
**Liu et al. 2026(*Frontiers in Neurology*, 중국 허난중의약대학)**
은 같은 비교(VM 60명 vs HC 20명)에서 **정반대 결과**(혈청 CGRP가 VM을 유의하게 판별, AUC=0.794)를 보고했다. (IF 3.1. Clinical characteristics and exploratory serum biomarker findings in vestibular migraine: a cross-sectional case–control study)

<img width="1069" height="613" alt="image" src="https://github.com/user-attachments/assets/66cf410c-ceb2-4a93-8f12-129d8f2442a2" />

-

<img width="1085" height="272" alt="image" src="https://github.com/user-attachments/assets/74ad9b07-84d7-4a83-9522-225d0ea6c393" />

-

<img width="1070" height="574" alt="image" src="https://github.com/user-attachments/assets/8ed8704b-115b-46d2-95eb-2628546864ee" />

Liu 논문은 단순 비교(AUC=0.794)뿐 아니라, CGRP·FGF-21·GDF-15 세 마커를 동시에 넣은 다변량 로지스틱 회귀 모델도 보고한다. 이 모델에서 CGRP 행의 수치는 아래와 같다.

| 항목 | 값 | 의미 |
|---|---|---|
| B (회귀계수) | 0.394 | CGRP가 10 pg/mL 오를 때 "VM일 로그오즈"가 0.394만큼 오른다는 뜻. |
| SE (표준오차) | 0.183 | B 추정치의 불확실성. 표본(80명)이 작아 값이 큰 편이다. |
| Wald χ² | 4.624 | "CGRP는 VM 여부와 무관하다(B=0)"는 가설을 검정하는 통계량. $(B/SE)^2 = (0.394/0.183)^2 \approx 4.62$. |
| P값 | 0.032 | 위 검정의 유의확률. FGF-21·GDF-15를 같이 통제한 상태에서도 CGRP는 유의하다(<0.05). |
| 보정 OR | 1.483 | 오즈비, $\exp(0.394)$. CGRP가 10 pg/mL 오를 때마다 "VM일 오즈"가 약 1.48배로 커진다. |
| 95% CI | 1.035–2.123 | $\exp(0.394 \pm 1.96\times0.183)$. 1을 포함하지 않아 P<0.05와 같은 결론을 재확인해준다. |

이 모델의 종속변수는 "VM 여부"(VM=1, 건강 대조군=0)이고, 독립변수는 CGRP·FGF-21·GDF-15(각각 10 pg/mL 단위) 세 개를 동시에 넣었다. 
- 즉 CGRP만 따로 본 게 아니라 "다른 두 마커를 고정했을 때 CGRP가 그래도 VM을 가르는가"를 검정한 결과다. 식으로 쓰면:

$$\text{logit}(P(\text{VM}=1)) = -2.612 + 0.394\,X_{\text{CGRP}} + 0.066\,X_{\text{FGF-21}} + 0.214\,X_{\text{GDF-15}}$$

---

#### 어떤 차이가 있지
**채혈 시점이 다른가?**
- CGRP가 혈중에서 빠르게 사라진다는 점(Kraenzlin et al. 1985)을 생각해 봄.

<img width="685" height="590" alt="image" src="https://github.com/user-attachments/assets/2c8083e3-237e-45a4-9476-f48361d7e7c0" />

<img width="761" height="90" alt="image" src="https://github.com/user-attachments/assets/5d777ad1-5c8c-40cd-a9b9-4c99403f8a67" />

그런데, 
- Liu도 Bai와 마찬가지로 **interictal(발작이 없는 시기)** 채혈이었고(최소 발작 후 경과시간은 기록 x),
- **Karlsson et al. 2026(*Neurology*, 편두통 588명 vs 대조군 147명, RIA 방식)**도 ictal-interictal 비교에서 유의한 차이가 없었다(p=0.092).

<img width="509" height="347" alt="image" src="https://github.com/user-attachments/assets/0232902c-1dec-4ff3-a1ff-71c06b6e24df" />

- 조사한 논문들을 종합해보면, 채혈 시점 때문에 CGRP의 유의함이 달라진 것 같지는 않다.

**그렇다면?**
조사로 확인 가능한 차이점은 **검체 종류와 분석 키트**였다
- Bai는 혈장(plasma)에 Bertin사 키트(A05481), Liu는 혈청(serum)에 Elabscience사 키트(E-EL-H0619)를 썼다.
- Karlsson(RIA)은 오히려 편두통군에서 CGRP가 **더 낮게**(125 vs 151 pmol/L, p<0.001) 나와 세 번째 방향을 제시했고, Discussion에서 **Garelja et al. 2025(*Headache*)**를 인용했다

| 연구 | 비교 대상 | 측정 검체 | 결과 방향 |
|---|---|---|---|
| Bai 2025 | VM vs HC | 혈장·타액 | 차이 없음(null) — 혈장 p=1.000, 타액 p=0.699 |
| Liu 2026 | VM vs HC | 혈청 | VM에서 더 높음(positive) — median 53.45 vs 18.58 pg/mL, p<0.01 |
| Karlsson 2026 | 편두통(일반) vs HC | 혈장 | 편두통에서 더 낮음(negative) — median 125 vs 151 pmol/L, p<0.001 |

- 이 연구는 CGRP ELISA 키트 두 종(Cusabio CSB-E08210h vs Bertin A05481)을 직접 비교해 Cusabio 키트가 실제 CGRP를 전혀 검출하지 못한다는 것(질량분석 결과 표준물질이 CGRP가 아니라 소혈청알부민이었음)을 밝혔고, 이 결함 키트를 쓴 기존 논문이 11편이라고 지적했다. Bai(Bertin)와 Liu(Elabscience)는 둘 다 이 "결함 키트"(Cusabio)를 쓴 건 아니라서 이 연구가 둘의 차이를 직접 설명하진 않지만, "CGRP ELISA 키트는 제조사에 따라 완전히 다른 걸 잴 수도 있다"는 걸 별도 전문(full text)으로 확인해주는 근거다.

> "Kit A did not detect bioactive forms of human α-CGRP or β-CGRP, nor mouse α-CGRP or β-CGRP." — Abstract, Results
>
> "We were unable to detect any CGRP-related peptides with mass spectrometry... the standard contains a complex matrix of other proteins, notably bovine serum albumin." — Discussion, p.1751
>
> "A CGRP ELISA kit produced by Cusabio (Cat# CSB-E08210h), that herein we refer to as 'Kit A,' has now been used by researchers in a range of patient samples, including plasma, tear fluid, saliva, and serum.3-8,12,14-17" — Introduction, p.1746
>
> Garelja ML, Rees TA, Hay DL. "Calcitonin gene-related peptide and headache: comparison of two commonly used assay kits highlights the perils of measuring neuropeptides with enzyme-linked immunosorbent assays." *Headache*. 2025;65(10):1744-1753. doi:10.1111/head.15011

정리하면 코펩틴/S100B와 달리 CGRP는 같은 질문("편두통군이 대조군과 CGRP가 다른가")에 대해 문헌마다 "높다/없다/낮다"로 답이 갈리고, 그 원인이 검체·키트·분석법 차이일 가능성이 문헌으로 뒷받침된다.

---

#### 남은 두 가지 유의점

**전처리 시점 가정도 같이 점검할 필요가 있다**
로드맵은 CGRP 반감기(10분 남짓)를 근거로 채혈~안정화까지의 전처리 시간을 핵심 변수로 본다. 이번에 검토한 세 연구(Bai, Liu, Karlsson)는 공통적으로 ictal-interictal(발작 중/발작 없음) 비교에서 유의차가 없었다 — 발작 시점 자체는 세 연구 모두에서 CGRP 수치를 가르는 요인으로 나타나지 않았다. 다만 이 세 연구가 본 건 "발작이냐 아니냐"라는 굵은 단위 구분이라, 분 단위의 미세한 전처리 지연 효과까지 배제한 건 아니다. 전처리 표준화가 여전히 유효한 설계 목표일 수 있으니, 세 연구가 공통으로 짚은 다른 원인(검체 종류·ELISA 키트)도 같이 고려 대상에 넣는 게 안전하다.

**항체 기반 키트는 실제로 표적을 재는지 별도 검증이 필요하다**
Garelja et al. 2025(*Headache*)는 질량분석으로 상용 CGRP ELISA 키트(Cusabio CSB-E08210h)의 표준물질이 CGRP가 아니라 소혈청알부민이었다는 걸 확인했고, 이 키트를 쓴 기존 논문이 11편이라고 지적했다. 카트리지에 쓸 항체/키트를 선정할 때, 이 논문이 쓴 검증 절차(스파이크 회수 실험 + 질량분석)를 참고할 수 있다.

---

- **눈물 AChR**은 아무도 해본 적 없는 영역이다. 참고할 선행 연구가 없다.

> 요약: 코펩틴+S100B 조합은 근거가 있고, CGRP와 눈물 AChR은 각각 다른 이유로 아직 확실하지 않다.

## PD 바이오마커 요약

30편을 조사했다. 
- 파킨슨병을 뇌스캔 없이 **혈액·침·눈물·땀·소변 같은 체액검사**로 진단할 수 있는지 논문 66편을 먼저 찾았고,
- 원문을 하나씩 대조해서 검증한 뒤 30편(45%)만 남겼고, 이에 대해 조사했다. 

### 혈액 - 13편
**혈액(13편)**: 가장 눈에 띄는 수치는 Chang(2020) 연구의 AUC 0.992다 — 1에 가까울수록 환자와 정상인을 거의 완벽하게 구분한다는 뜻인데, 이건 PD 48명·정상인 40명이라는 작은 표본 1건에서 나온 값이라 그대로 믿기는 이르다. 반대로 Qu(2023)는 152편을 묶은 메타분석으로 PD 9,032명·정상인 12,628명을 봤는데, 여기서는 염증 수치(IL-6, IL-1β)가 PD에서 꾸준히 높게 나온다는, 덜 극적이지만 훨씬 큰 근거로 뒷받침되는 결과를 보여준다. miRNA 조합을 본 Guévremont(2023) 메타분석은 AUC 0.87로 중간 정도다.

**침(타액, 8편)**: 여기가 가장 믿을 만하다. Rastogi(2023)는 AUC 0.9674로 최고 수치를 냈고, Kharel(2022) 메타분석(13편)도 같은 단백질(올리고머 알파시누클레인)이 PD에서 뚜렷하게 증가한다고(SMD 2.88) 확인했다. Costanzo(2024)도 AUC 0.8487로 비슷한 결과를 냈다. 서로 다른 세 팀이 독립적으로 같은 단백질에서 같은 방향의 결과를 낸 셈이라, 우연히 한 번 잘 나온 값이 아니라는 근거가 된다.

**눈물(5편)**: 뭘 재느냐에 따라 결과가 완전히 갈린다. Costanzo(2026)가 RT-QuIC이라는 방법(단백질이 비정상적으로 뭉치는 성질을 감지하는 검사)으로 재면 아주 강한 차이(p<0.0001)가 나오지만, Maass(2020)가 단백질 총량만 재면 판별력이 약하다(AUROC 0.60 — 절반보다 살짝 나은 수준). 방법을 잘못 고르면 같은 체액에서도 쓸모없는 결과가 나올 수 있다는 뜻이다.

**땀·피지(1편)**: Trivedi(2019) 한 편뿐이다. 피지의 휘발성 화합물 두 가지가 PD에서 늘고 줄었다는 결과지만, 독립적으로 재확인한 연구가 없어 검증됐다고 말하기는 이르다.

**소변(3편)**: 원래 검색에서는 13편이 걸렸지만, 하나하나 확인하니 10편이 실제로는 혈액이나 뇌척수액을 다룬 연구를 소변 연구로 잘못 분류해놓은 것이었다. 진짜 소변 특이적 근거는 Winter(2021, 단백질 361종 차이, 판별 모델 민감도 78%·특이도 73%)와 Dhiman(2025) 메타분석 등 3편뿐이라, 다섯 체액 중 근거가 가장 얇다.


---

[← 홈으로]({{ '/' | relative_url }})
