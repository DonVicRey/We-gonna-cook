from flask import Flask, request, jsonify
from flask_cors import CORS
import ctypes
import os
import sys

app = Flask(__name__)
CORS(app) # Permits cross-origin requests from browser components or extensions

# Determine binary file extension type based on your Host operating system
if sys.platform == "win32":
    binary_name = "core_system.dll"
else:
    binary_name = "./core_system.so"

lib_path = os.path.abspath(binary_name)

# Mount the compiled C/C++ Shared Library Core
try:
    jarvis_core = ctypes.CDLL(lib_path)
    # Define argument mapping configurations for memory safety
    jarvis_core.execute_hardware_diagnostic.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
    jarvis_core.execute_hardware_diagnostic.restype = None
    print(">>> SUCCESS: Starktech C/C++ Shared Library matrix loaded.")
except Exception as e:
    print(f">>> CRITICAL: C/C++ Library could not be mapped: {e}")
    jarvis_core = None

@app.route('/api/command', methods=['POST'])
def handle_command():
    data = request.json or {}
    user_message = data.get("command", "").lower()
    
    reply = "Instruction processed through secondary cloud neural channels."
    
    # Keyword detection filters routing workloads to the local C/C++ module
    if "status" in user_message or "diagnostic" in user_message:
        if jarvis_core:
            # Allocate a mutable string buffer in memory for C/C++ to safely modify
            buf_size = 256
            c_buffer = ctypes.create_string_buffer(buf_size)
            
            # Fire the compiled C++ code directly (Passing ID 1)
            jarvis_core.execute_hardware_diagnostic(1, c_buffer, buf_size)
            reply = c_buffer.value.decode('utf-8')
        else:
            reply = "C-Core sub-module uninitialized. Check local compilation layers."
            
    elif "speed" in user_message or "matrix" in user_message:
        if jarvis_core:
            buf_size = 256
            c_buffer = ctypes.create_string_buffer(buf_size)
            jarvis_core.execute_hardware_diagnostic(2, c_buffer, buf_size)
            reply = c_buffer.value.decode('utf-8')
            
    elif "hello" in user_message or "jarvis" in user_message:
        reply = "Systems initialized, sir. Python API server and compiled C code structures are communicating flawlessly."

    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
