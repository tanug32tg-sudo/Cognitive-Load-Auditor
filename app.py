import os
import csv
import time
from playwright.sync_api import sync_playwright
import google.generativeai as genai

# --- CONFIGURATION ---
# Paste your Key here (Make sure to remove 'python app.py' if it's there!)
API_KEY = "PASTE_YOUR_GOOGLE_API_KEY_HERE"

# List of websites to audit
TEST_SUITE = [
    "https://www.wikipedia.org/",
    "https://www.google.com/",
    "https://www.bbc.com/" 
]

def analyze_screenshot(image_path):
    """Sends image to AI and asks for a strict friction score."""
    genai.configure(api_key=API_KEY)
    
    # Using your working model
    model = genai.GenerativeModel('gemini-3-flash-preview')
    
    sample_file = genai.upload_file(path=image_path, display_name="Website Screenshot")
    
    # We ask the AI to return data in a specific format for our report
    prompt = """
    Act as a Senior QA Specialist. Analyze this UI.
    Return ONLY a single line of text in this exact format:
    Score (0-10) | One specific UX issue | One specific fix
    
    Example:
    8/10 | Navigation bar is cluttered | Group links into a dropdown menu
    """
    
    response = model.generate_content([sample_file, prompt])
    return response.text.strip()

def main():
    # Create a CSV file to save our results
    with open('ux_audit_report.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["URL", "AI Analysis"]) # Header row

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            
            for url in TEST_SUITE:
                print(f"\n🚗 Navigating to: {url}")
                try:
                    page = browser.new_page()
                    page.goto(url)
                    time.sleep(2) # Wait for page to load
                    
                    # Take screenshot
                    screenshot_name = "temp_screen.png"
                    page.screenshot(path=screenshot_name)
                    
                    # Ask AI
                    print("🤖 Analyzing UX Friction...")
                    result = analyze_screenshot(screenshot_name)
                    
                    # Save to File
                    writer.writerow([url, result])
                    print(f"✅ Result Saved: {result}")
                    
                    page.close()
                except Exception as e:
                    print(f"❌ Failed to test {url}: {e}")
            
            browser.close()
            print("\n" + "="*40)
            print("🎉 AUDIT COMPLETE! Open 'ux_audit_report.csv' to see results.")
            print("="*40)

if __name__ == "__main__":
    main()