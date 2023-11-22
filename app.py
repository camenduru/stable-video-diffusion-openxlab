from notebook.app import main
main(["--port", str(7860), "--ip", "0.0.0.0", "--NotebookApp.token", "", "--no-browser", "--NotebookApp.tornado_settings", "{'headers': {'Content-Security-Policy': 'frame-ancestors *'}}"])
