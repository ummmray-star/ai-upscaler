import cv2
import time
import numpy as np
import psutil
from typing import List, Tuple

# Function to detect hardware specifications

def detect_hardware() -> str:
    cpu_info = psutil.cpu_info()
    ram_info = psutil.virtual_memory()
    hardware_details = (f"CPU: {cpu_info.brand_raw}, {cpu_info.physical_cores} cores, {cpu_info.max_freq}MHz\n" 
                      f"RAM: {ram_info.total // (1024 * 1024)} MB total\n")
    return hardware_details

# Function to benchmark inference speed

def benchmark_inference(model, image: np.ndarray, resolutions: List[Tuple[int, int]]) -> None:
    results = []
    for resolution in resolutions:
        # Resize image to the target resolution
        resized_image = cv2.resize(image, resolution)
        start_time = time.time()
        # Perform the inference (this is a placeholder for the actual model call)
        # output = model.infer(resized_image)
        end_time = time.time()
        inference_time = end_time - start_time
        results.append((resolution, inference_time))
    print("Inference Speed Benchmark:")
    for resolution, duration in results:
        print(f'Resolution: {resolution}, Inference Time: {duration:.6f} seconds')

if __name__ == '__main__':
    # Example usage
    # Load your model here (placeholder)
    # model = load_model('path_to_your_model')
    # Load a sample image
    image_path = 'path_to_your_image.jpg'
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not load image.")
    else:
        hardware = detect_hardware()
        print(hardware)
        # Define resolutions to test
        resolutions_to_test = [(640, 480), (1280, 720), (1920, 1080), (3840, 2160)]
        benchmark_inference(None, image, resolutions_to_test)