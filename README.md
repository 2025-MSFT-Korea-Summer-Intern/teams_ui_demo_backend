```markdown
## 서버 실행 방법

1. Conda 환경 활성화 또는 생성  
    - 환경이 없으면 Python 3.10로 생성:
        ```bash
        conda create -n term_tracker_back_demo python=3.10
        conda activate term_tracker_back_demo
        ```
    - 환경이 이미 있으면 활성화:
        ```bash
        conda activate term_tracker_back_demo
        ```

2. 필요한 패키지 설치
    ```bash
    python -m pip install -r requirements.txt
    ```

3. 서버 실행
    ```bash
    python -m uvicorn main:app --reload
    ```
```