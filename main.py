import cv2
import argparse
import sympy as sp

from preprocess import preprocess_image
from segment import segment_characters
from recognize import recognize_symbols
from solver import solve_equation

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Handwritten Equation Solver")
    parser.add_argument("--image", type=str, required=True, help="Path to input image")
    args = parser.parse_args()

    image = cv2.imread(args.image)
    processed = preprocess_image(image)
    chars = segment_characters(processed)
    equation_str = recognize_symbols(chars)
    print(f"Equation Detected: {equation_str}")
    solution = solve_equation(equation_str)
    print("Solution:")
    print(solution)
