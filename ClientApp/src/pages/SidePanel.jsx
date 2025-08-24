import { useEffect, useState } from "react";
import * as microsoftTeams from "@microsoft/teams-js";
import { useTermCardStyles } from "../styles/styles";

// 반드시 해야하는 것
// 1. {process.env.WS_ENDPOINT}/meeting/${meetingId}/terms 참고해서 받아올 수 있도록 백엔드랑 협업하기.
// 2. 디자인, CSS 설정
// ===================================================
// 추천하는 것
// 1. 필터링
// 2. 클릭하면 열리거나 이동


const SidePanel = (props) => {

    const contextRef = useRef(null);
    const wsRef = useRef(null);
    const termListRef = useRef([]);

    const [appTheme, setAppTheme] = useState("");
    const [termList, setTermList] = useState([]);

    useEffect(() => {
        (async () => {
            await microsoftTeams.app.initialize();

            // 1. 일단 지금 미팅의 정보를 가져오시오.
            const context = await microsoftTeams.app.getContext();
            contextRef.current = context;

            // 2. 그리고 테마 먼저 수정하겠소.
            handleThemeChange(context.app.theme);
            microsoftTeams.app.registerOnThemeChangeHandler(handleThemeChange);

            // 3. 미팅 ID를 통해 WebSocket 연결을 생성하겠소.
            wsRef.current = createWebSocket(context.meeting.meetingId);
        });

        return () => {
            if (wsRef.current) wsRef.current.close();
        };
        }, []
    );

    useEffect(() => {
        setTermList([...termListRef.current]);
        }, [termListRef.current.length]
    );
    
    function handleThemeChange(theme) {
        switch (theme) {
            case 'dark':
                setAppTheme('theme-dark');
                break;
            case 'default':
                setAppTheme('theme-light');
                break;
            case 'contrast':
                setAppTheme('theme-contrast');
                break;
            default:
                setAppTheme('theme-light');
        }
    }

    function createWebSocket(meetingId) {
        const ws = connectWebSocket(meetingId);
        ws.onopen = () => setErrorMsg(
            "" // 연결 성공 시 에러 메시지 초기화
        ); 
        ws.onerror = () => setErrorMsg(
            "웹소켓 연결에 실패했습니다."
        );
        ws.onmessage = (event) => handleWebSocketMessage(event);
        return ws;
    }

    function connectWebSocket(meetingId) {
        const wsEndpoint = `${process.env.REACT_APP_WS_ENDPOINT}/meeting/${meetingId}/terms`;
        return new WebSocket(wsEndpoint);
    }

    function handleWebSocketMessage(event) {
        try {
            const data = JSON.parse(event.data);
            // { term_list: [ { ...TermInfo }, ... ] }
            const term_list = data.term_list;
            if (Array.isArray(term_list)) {
                const newTerms = term_list.filter(
                    item => !termListRef.current.some(term => term.id === item.id)
                );
                termListRef.current = [
                    ...termListRef.current,
                    ...newTerms
                ].sort((a, b) => new Date(a.timestamp) - new Date(b.timestamp));
            }
        } catch (error) {
            setErrorMsg("데이터 처리 중 오류가 발생했습니다.");
        }
    }

    function RenderTerm({ term }) {
        const styles = useTermCardStyles();
        return (
            <li style={{ listStyle: "none" }}>
                <div className={styles.card}>
                    <span className={styles.term}>{term.term}</span>
                    <span className={styles.category}>{term.category}</span>
                    <span className={styles.explanation}>{term.explanation}</span>
                </div>
            </li>
        );
    }

    return (
        <div className={appTheme}>
            <div id="list">
                <ol type="1" id="termList">
                    {termList.map(term => (
                        <RenderTerm key={term.id} term={term} />
                    ))}
                </ol>
            </div>
        </div>
    );
};

export default SidePanel;