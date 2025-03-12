## OCR 성능 개선

OCR 인식률 향상을 위한 이미지 전처리 기술 구현 및 비교(개인 프로젝트)

</br>

## 주요 기능

이미지 내 글씨 흐림 및 그림자로 인해 발생하는 OCR 인식률 저하 문제를 해결하는 것을 목표로 합니다.
</br> Fine-tuning과 같은 기존 방식으로 접근한 것이 아닌, 경량화와 효율적인 계산 시간을 고려하여 근본적인 여러 이미지 전처리 방식을 사용합니다.
</br> 이를 통해 다양한 환경에서도 안정적인 문자 인식을 가능하게 하며, 서비스의 활용도를 극대화합니다.

</br>

## 대표 적용 예시

|원본|흑백|흑백 + CLAHE|그림자 제거 + 배경 제거 + CLAHE|그림자 제거 + 배경 제거 + Prewitt Edge|그림자 제거 + 배경 제거 + Mean Adaptive Thresholding|
|:---:|:---:|:---:|:---:|:---:|:---:|
|<img src="https://github.com/user-attachments/assets/f918abd0-ac2b-436f-8d26-ac804facd591" width="200" height="200" />|<img src="https://github.com/user-attachments/assets/4ae7abb1-cb54-4721-9b4e-da5da0e613b8" width="200" height="200" />|<img src="https://github.com/user-attachments/assets/ec93317c-f3ff-49b5-b46b-3fe8fd2fd803" width="200" height="200" />|<img src="https://github.com/user-attachments/assets/4b365c8e-03fd-45f6-bae0-3b99dd0d3d03" width="200" height="200" />|<img src="https://github.com/user-attachments/assets/32f61705-b2c6-4eca-866f-686d1e7a7c65" width="200" height="200" />|<img src="https://github.com/user-attachments/assets/32f61705-b2c6-4eca-866f-686d1e7a7c65" width="150" height="200" />|

</br>

## 차별성

<img src=https://github.com/user-attachments/assets/c6a09139-4af5-41fe-9b28-cd0b7595f002 height="700px">

GUI 기반으로, 다운로드 후 실시간으로 적용 결과를 즉시 확인할 수 있어 직관적인 사용자 경험을 제공합니다.

</br>

## TooL

`OpenCV` `Numpy` `OpenCV` `Matplotlib` `PyQt`

</br>

## 다운로드

[RCH_image_OCR_processor.exe](https://github.com/Ryuchanghoon/Improve-OCR-Quality/blob/main/improve_OCR_processor/RCH_image_OCR_processor.exe)

</br>

## OCR 성능 개선 프로젝트 스토리

[OCR 성능 끌어올리기 1st step](https://velog.io/@fbckdgns3/OCR-%EC%84%B1%EB%8A%A5-%EB%81%8C%EC%96%B4%EC%98%AC%EB%A6%AC%EA%B8%B0-1st-step)
</br>[OCR 성능 끌어올리기 2nd step: Binarization-1](https://velog.io/@fbckdgns3/OCR-%EC%84%B1%EB%8A%A5-%EB%81%8C%EC%96%B4%EC%98%AC%EB%A6%AC%EA%B8%B0-2nd-step#--manual-thresholding%EC%88%98%EB%8F%99-%EC%9E%84%EA%B3%84%EA%B0%92)
</br>[OCR 성능 끌어올리기 2nd step: Binarization-2](https://velog.io/@fbckdgns3/OCR-%EC%84%B1%EB%8A%A5-%EB%81%8C%EC%96%B4%EC%98%AC%EB%A6%AC%EA%B8%B0-2nd-step-Binarization-2)
</br>[OCR 성능 끌어올리기 3rd step: Reducing noise-1](https://velog.io/@fbckdgns3/OCR-%EC%84%B1%EB%8A%A5-%EB%81%8C%EC%96%B4%EC%98%AC%EB%A6%AC%EA%B8%B0-3rd-step-Reducing-noise-1)
</br>[OCR 성능 끌어올리기 3rd step: Reducing noise-2](https://velog.io/@fbckdgns3/OCR-%EC%84%B1%EB%8A%A5-%EB%81%8C%EC%96%B4%EC%98%AC%EB%A6%AC%EA%B8%B0-3rd-step-Reducing-noise-2)
</br>[OCR 성능 끌어올리기 4th step: Reducing shadow](https://velog.io/@fbckdgns3/OCR-%EC%84%B1%EB%8A%A5-%EB%81%8C%EC%96%B4%EC%98%AC%EB%A6%AC%EA%B8%B0-4th-step-Reducing-shadow)
</br>[OCR 성능 끌어올리기 5th step: edge detection](https://velog.io/@fbckdgns3/OCR-%EC%84%B1%EB%8A%A5-%EB%81%8C%EC%96%B4%EC%98%AC%EB%A6%AC%EA%B8%B0-5th-step-edge-detection)
</br>[OCR 성능 끌어올리기 6th step: Bounding box & Contour](https://velog.io/@fbckdgns3/OCR-%EC%84%B1%EB%8A%A5-%EB%81%8C%EC%96%B4%EC%98%AC%EB%A6%AC%EA%B8%B0-6th-step-Bounding-box-Contour)
</br>[OCR 성능 끌어올리기 7th step: Compare](https://velog.io/@fbckdgns3/OCR-%EC%84%B1%EB%8A%A5-%EB%81%8C%EC%96%B4%EC%98%AC%EB%A6%AC%EA%B8%B0-7th-step-Compare)
</br>[OCR 성능 끌어올리기 8th step: ReCompare](https://velog.io/@fbckdgns3/OCR-%EC%84%B1%EB%8A%A5-%EB%81%8C%EC%96%B4%EC%98%AC%EB%A6%AC%EA%B8%B0-8th-step-ReCompare)
</br>[OCR 성능 끌어올리기: 이미지 전처리 프로그램](https://velog.io/@fbckdgns3/OCR-%EC%84%B1%EB%8A%A5-%EB%81%8C%EC%96%B4%EC%98%AC%EB%A6%AC%EA%B8%B0-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%A0%84%EC%B2%98%EB%A6%AC-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8)
[OCR 성능 끌어올리기 Final](https://velog.io/@fbckdgns3/OCR-%EC%84%B1%EB%8A%A5-%EB%81%8C%EC%96%B4%EC%98%AC%EB%A6%AC%EA%B8%B0-Final)
