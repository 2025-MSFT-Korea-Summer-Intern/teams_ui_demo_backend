```markdown
## 서버 실행 방법

1. Run ngrok - point to port 3000 (pointing to ClientApp)

   ```bash
   ngrok http 3001 --host-header="localhost:3000"
   ```  

2. 필요한 패키지 설치
    ```bash
    npm install
    ```

3. 서버 실행
    ```bash
    npm start
    ```
```