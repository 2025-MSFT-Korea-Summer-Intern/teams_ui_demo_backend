/*!
 * Copyright (c) Microsoft Corporation. All rights reserved.
 * Licensed under the MIT License.
 */

import { makeStyles, shorthands } from "@fluentui/react-components";

export const getVideoStyle = makeStyles({
  root: {
    cursor: "pointer",
    minWidth: "100%",
    minHeight: "100%",
    maxHeight: "100%",
    maxWidth: "100%",
    left: "50%",
    top: "50%",
    bottom: "50%",
    right: "50%",
    zIndex: 0,
    position: "fixed",
    transform: "translate(-50%, -50%)",
  },
});

export const getPlayerControlStyles = makeStyles({
  pointerTrackerContainer: {
    position: "absolute",
    zIndex: 0,
    top: "0",
    right: "0",
    left: "0",
    bottom: "0",
  },
});

export const getProgressBarStyles = makeStyles({
  root: {
    width: "100%",
    cursor: "pointer",
    minHeight: "0px",
  },
  input: {
    cursor: "pointer",
  },
  rail: {
    backgroundImage: `linear-gradient(
      to right,  
      rgba(255,255,255, 1) 0%, 
      rgba(255,255,255,1) var(--oneplayer-play-progress-percent), 
      rgba(255,255,255,0.5) var(--oneplayer-play-progress-percent), 
      rgba(255,255,255,0.5) var(--oneplayer-buff-progress-percent),  
      rgba(255,255,255,0.3) var(--oneplayer-buff-progress-percent), 
      rgba(255,255,255,0.3) 100%)
    `,
    ":before": {
      backgroundImage: "none",
    },
  },
  thumb: {
    width: "1.2rem",
    height: "1.2rem",
    backgroundColor: "white",
    boxShadow: "none",
    ":before": {
      ...shorthands.borderColor("white"),
    },
  },
  pageEl: {
    backgroundColor: "transparent",
    color: "white",
    ...shorthands.padding(".6rem"),
  },
});

export const useTermCardStyles = makeStyles({
    card: {
        background: "var(--colorNeutralBackground1)",
        boxShadow: "0 2px 8px rgba(0,0,0,0.08)",
        borderRadius: "8px",
        padding: "16px",
        marginBottom: "12px",
        display: "flex",
        flexDirection: "column",
        gap: "8px",
    },
    term: {
        fontWeight: 600,
        fontSize: "16px",
        color: "var(--colorNeutralForeground1)",
    },
    category: {
        fontSize: "14px",
        color: "var(--colorNeutralForeground2)",
    },
    explanation: {
        fontSize: "13px",
        color: "var(--colorNeutralForeground3)",
    },
});