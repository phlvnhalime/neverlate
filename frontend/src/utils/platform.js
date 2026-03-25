export const isTauri = () => {
    return window && window.__TAURI_INTERNALS__ !== undefined;
};