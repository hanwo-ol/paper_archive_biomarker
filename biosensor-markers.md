---
layout: page
title: KIST-JBNU 바이오센서 마커
permalink: /biosensor-markers/
---

# 다중 바이오센서 카트리지 후보 마커 문헌 근거

JBNU 전북대학교병원 × KIST 생체분자인식연구센터 공동연구과제 · 2026-09-21

이 문서는 카트리지 후보 마커(혈액 코펩틴/S100β, 타액 CGRP, 눈물 anti-AChR)별로 논문이 실제로 무엇을 보고했는지 정리한다. 통계적 재산정(표본크기·검정력 계산)은 다루지 않는다.

쉽게 풀어쓴 버전은 [여기]({{ '/eli5/' | relative_url }})에 있다.

## 혈액: 코펩틴 / 코펩틴+S100β (AVS·뇌졸중 rule-out)

AVS(Acute Vestibular Syndrome, 급성전정증후군)는 갑자기 시작해 24시간 이상 지속되는 어지럼증으로, 원인이 말초성(전정신경염, 양성)이거나 중추성(소뇌·뇌간 뇌졸중, 응급)이다. 아래 논문들은 혈액 마커로 이 둘을 구분하는 rule-out 검사로서의 코펩틴·S100β 성능을 보고한다.

| 논문 | 실제 보고 내용 |
|---|---|
| Deboevere et al. 2019, *Scand J Trauma Resusc Emerg Med* | N=135(뇌졸중 확진 13, 비뇌졸중 122). 코펩틴 단독 민감도 76.9%(10/13)·특이도 50%·NPV 93%. 코펩틴+S100β 병합(둘 중 하나라도 양성) 민감도 100%(13/13)·특이도 48%·NPV 100%. 저자 결론: "대규모 검증이 필요하다"(pending larger-scale validation). |
| Klokman et al. 2024, *Acad Emerg Med* (체계적 문헌고찰·메타분석, 17편·61개 마커) | 코펩틴·S100β·NSE를 포함한 "뇌 유래 바이오마커"가 응급실 AVS 환자에서 중추성·말초성 원인을 유의하게 구분한다고 보고. |
| von Recum et al. 2015, *Stroke Res Treat* | 코펩틴 단독의 뇌졸중 감별 정확도는 63%, 민감도 80%에 그쳤고, 뇌졸중 모방질환(stroke mimic)에서 코펩틴 수치의 변동 폭이 넓어 판별력을 제한한다고 보고. |

> 코펩틴 단독은 논문마다 민감도가 77~80%로 일관되게 부족하다 — rule-out 검사로 쓰면 뇌졸중 환자 4~5명 중 1명을 놓칠 수 있다는 뜻이다. S100β를 더해 병합 판정(OR 규칙)을 쓰면 같은 파일럿에서 민감도가 100%까지 올라간다. 이 병합 패널 아이디어는 Deboevere 2019 단일 논문(뇌졸중 확진 13명 파일럿)에 근거하며, 저자 본인이 대규모 검증이 필요하다고 명시했다 — 이 카트리지 조합을 채택하는 근거는 있지만, 검증 규모를 키우는 것이 다음 단계로 남아 있다.

## 타액: CGRP (편두통)

| 논문 | 실제 보고 내용 |
|---|---|
| Alpuente et al. 2022, *Cephalalgia* 42(3):186-196 | 삽화편두통 환자 22명 vs 건강대조군 22명의 interictal(발작간기) 타액 CGRP 비교 — 환자군 median 98.0 pg/mL, 대조군 median 54.3 pg/mL, p=0.034로 유의한 차이. 발작 중에는 preictal→ictal(0h)에서 CGRP가 급상승(164.6 pg/mL)한 뒤 발작 후 감소하는 패턴을 확인. |
| Bai, Chu, Kang, Chae, Dieterich, Oh 2025, *Cephalalgia* | 전정편두통(VM) 환자 81명, 만성편두통(CM) 환자 73명, 건강대조군 59명의 interictal 혈장·타액 CGRP 비교 — VM은 CM보다 유의하게 낮았으나(혈장 median 37.1 vs 74.6 pg/mL, p<0.001), **VM과 건강대조군 사이에는 유의한 차이가 없었다.** 저자 결론: "interictal plasma and salivary CGRP levels are unlikely to serve as biomarkers for VM." |

> 타액 CGRP는 일반 편두통(삽화편두통) 환자와 대조군을 구분하는 근거는 있다(Alpuente 2022). 그러나 이 협업이 실제로 다루는 임상군인 전정편두통(VM)에서는, JBNU 연구진이 직접 발표한 2025년 논문이 CGRP가 건강대조군과 구분되지 않는다고 결론 내렸다. CGRP를 VM 진단 마커로 카트리지에 포함하려면, 자체 데이터가 이미 부정적이라는 점을 미팅에서 먼저 밝히고 채택 여부를 논의해야 한다.

## 눈물: anti-AChR (MG-Sentinel)

Europe PMC·CrossRef에서 "tear/tear fluid + acetylcholine receptor + antibody" 조합으로 두 차례 검색(bibliographic 8건, 전문검색 15건)했다. 두 검색 모두 혈청(serum) anti-AChR 연구만 나왔고, 눈물(tear fluid) 특이적 anti-AChR 연구는 확인되지 않았다.

> 이 마커는 선행문헌이 없는 신규 검체·신규 분석 조합이다. 혈청 anti-AChR은 중증근무력증(MG) 임상 진단에서 널리 쓰이는 확립된 검사이지만, 눈물 검체에서의 민감도·특이도를 뒷받침하는 문헌은 검색 결과 존재하지 않는다. 카트리지 설계에 포함하려면 자체 파일럿 데이터로 처음부터 검증해야 하는 마커라는 점을 그대로 전달하는 것이 맞다.

---

문헌 검색: Europe PMC, CrossRef API (2026-09-21 기준)

[← 홈으로]({{ '/' | relative_url }})
