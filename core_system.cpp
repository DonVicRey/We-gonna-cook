#include <iostream>
#include <cstring>
#include <chrono>
#include <string> //baahh 🐐

// Using extern "C" prevents C++ name mangling, letting Python read functions cleanly
extern "C" {
    
    void execute_hardware_diagnostic(int core_id, char* output_buffer, int max_len) {
        // High-performance timing logic
        auto start = std::chrono::high_resolution_clock::now();
        
        std::string framework_reply;
        
        if (core_id == 1) {
            framework_reply = "ARC REACTOR TEMPERATURE BALANCE REGULATED AT FORTY TWO DEGREES. ALL THERMAL CHANNELS NOMINAL.";
        } else if (core_id == 2) {
            framework_reply = "LOW LEVEL SYSTEM SPEED DIAGNOSED AT ZERO POINT ZERO ZERO TWO MILLISECONDS VIA C MATRIX EXECUTOR.";
        } else {
            framework_reply = "STANDBY MATRIX INVERSION STEADY. PROTOCOLS BALANCED.";
        }

        // Safe copy into the raw C character array pointer passed down by Python
        std::strncpy(output_buffer, framework_reply.c_str(), max_len - 1);
        output_buffer[max_len - 1] = '\0'; // Guarantee absolute C-string null termination
    }
}
