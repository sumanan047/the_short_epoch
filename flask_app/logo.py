import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.lines import Line2D
from PIL import Image

def create_logo(lw = 10, output_dir='.'):
    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(5, 5)) # Increased figure size for higher resolution
    # Add a white circle patch
    circle = patches.Circle((0.5, 0.5), 0.25, linewidth=2*lw, edgecolor='r', facecolor='none')
    ax.add_patch(circle)
    # Add a black arc patch
    arc = patches.Arc((0.5, 0.5), 0.5, 0.5, theta1=90, theta2=270, linewidth=3*lw, edgecolor='black', facecolor='none')
    ax.add_patch(arc)
    # Add a red line from the center with orientation 270 degrees
    line = Line2D([0.5, 0.5], [0, 0.5], linewidth=2*lw, color='red')
    ax.add_line(line)  # Use add_line instead of add_patch for Line2D
    # Add a black line from the center with orientation 90 degrees
    line = Line2D([0.5, 0.5], [0.5, 1.0], linewidth=3*lw, color='black')
    ax.add_line(line)  # Use add_line instead of add_patch for Line2D
    # Set axis limits
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    # Ensure the aspect ratio is 1:1 to prevent stretching
    ax.set_aspect('equal')
    ax.axis('off')
    # Save the figure as a PNG file in the specified output directory
    output_path = os.path.join(output_dir, 'theshortepochlogo.png')
    fig.savefig(output_path, dpi=2000) # Save as PNG for better quality and specify DPI
    return None

def remove_background(input_path, output_path):
    img = Image.open(input_path)
    img_np = np.array(img)
    # Assuming white background, change as needed
    white_color = np.array([255, 255, 255, 255])
    mask = np.all(img_np == white_color, axis=-1)
    img_np[mask] = [0, 0, 0, 0]  # Make background transparent
    img_transparent = Image.fromarray(img_np)
    img_transparent.save(output_path)

def png_to_ico(png_path, ico_path):
    """
    Converts a PNG image to an ICO file.

    Args:
        png_path: Path to the input PNG image file.
        ico_path: Path to the output ICO file.
        sizes: A list of icon sizes to include in the ICO file.
    """
    # Load the PNG image
    png_path = 'static/images/theshortepochlogo.png'
    img = Image.open(png_path)

    # Resize the image to 16x16
    img_resized = img.resize((32, 32))

    # Save the resized image as ICO
    ico_path = 'static/images/theshortepochlogo.ico'
    img_resized.save(ico_path, format='ICO')



if __name__ == "__main__":
    create_logo(lw=20,output_dir='static/images')
    remove_background('static/images/theshortepochlogo.png', 'static/images/theshortepochlogo.png')
    png_to_ico('static/images/theshortepochlogo.png', 'static/images/theshortepochlogo.ico')
