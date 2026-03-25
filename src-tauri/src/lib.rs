use tauri_plugin_shell::ShellExt;
use tauri_plugin_shell::process::CommandEvent;

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_shell::init())
        .plugin(tauri_plugin_notification::init())
        // .plugin(tauri_plugin_autostart::Builder::new().build())
        .setup(|app| {
            // initialize Autostart
            app.handle().plugin(tauri_plugin_autostart::init(
                tauri_plugin_autostart::MacosLauncher::LaunchAgent,
                Some(vec!["--slient"]),
            ))?;
            //start the Node.js process
            let (mut rx, _child) = app.shell()
            .sidecar("neverlate-node")
            .unwrap()
            .spawn()
            .expect("Failed to spawn sidecar");

            //listen for the Node.js process output
            tauri::async_runtime::spawn(async move {
                while let Some(event) = rx.recv().await {
                    if let CommandEvent::Stdout(line) = event {
                        println!("Sidecar says: {}", String::from_utf8_lossy(&line));
                    }
                }
            });
            
            if cfg!(debug_assertions) {
                app.handle().plugin(
                    tauri_plugin_log::Builder::default()
                        .level(log::LevelFilter::Info)
                        .build(),
                )?;
            }
            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
