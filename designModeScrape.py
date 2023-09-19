# https://chat.openai.com/share/ec305005-2ed7-4505-ac40-8252709fd2a3

from bs4 import BeautifulSoup

def extract_strings(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    results = []

    # Extract content between <label></label> tags
    for label in soup.find_all('label'):
        results.append(("label", label.get('id', 'no-id'), label.get_text()))

    # Extract content between <option></option> tags
    for option in soup.find_all('option'):
        select_id = option.find_parent('select').get('id', 'no-id')
        results.append(("dropdown", select_id, option.get_text()))

    # Extract content between <button></button> tags
    for button in soup.find_all('button'):
        results.append(("button", button.get('id', 'no-id'), button.get_text()))

    # Extract content within the 'placeholder' property of <input> elements
    for inp in soup.find_all('input'):
        if 'input' in inp.attrs:
            results.append(("input placeholder", inp.get('id', 'no-id'), inp['placeholder']))

    # Extract strings within <div></div> tags that have a contenteditable=true property
    for div in soup.find_all('div', contenteditable='true'):
        results.append(("textarea", div.get('id', 'no-id'), div.get_text()))

    return results

# Sample input
html_input = """
<div id="designModeViz" class="appModern clip-content" tabindex="1" data-radium="true" style="width: 320px; height: 450px; display: none;"><div class="screen" tabindex="1" data-theme="default" id="compressScreen" style="display: block; height: 450px; width: 320px; left: 0px; top: 0px; position: absolute; z-index: 0; background-color: rgb(27, 137, 247);"><input type="range" value="1" min="1" max="3000" step="1" id="bitsSlider" style="margin: 0px; padding: 0px; width: 310px; height: 25px; position: absolute; left: 5px; top: 305px;"><label style="margin: 0px; line-height: 1; overflow: hidden; overflow-wrap: break-word; max-width: 320px; border-style: solid; border-radius: 0px; border-width: 0px; border-color: rgb(77, 87, 95); color: rgb(255, 255, 255); font-family: &quot;Arial Black&quot;, Gadget, sans-serif; font-size: 16px; padding: 2px 15px; width: 90px; height: 20px; position: absolute; left: 220px; top: 425px; text-align: left; background-color: rgba(0, 0, 0, 0); text-rendering: optimizespeed;" id="sampleSizeOutput" class="design-mode-hidden"></label><label style="margin: 0px; line-height: 1; overflow: hidden; overflow-wrap: break-word; max-width: 320px; border-style: solid; color: rgb(255, 255, 255); background-color: rgba(0, 0, 0, 0); border-radius: 0px; border-width: 0px; font-family: Arial, Helvetica, sans-serif; font-size: 15px; padding: 2px 15px; width: 320px; height: 45px; position: absolute; left: -1.11022e-16px; top: 335px; text-align: center; border-color: rgb(0, 0, 0); text-rendering: optimizespeed;" id="label1">Move the slider to add more or less generations of noise to the image</label><label style="margin: 0px; line-height: 1; overflow: hidden; overflow-wrap: break-word; max-width: 320px; border-style: solid; border-radius: 0px; border-width: 0px; border-color: rgb(77, 87, 95); color: rgb(255, 164, 0); font-family: &quot;Arial Black&quot;, Gadget, sans-serif; font-size: 16px; padding: 2px 15px; width: 198px; height: 21px; position: absolute; top: 425px; text-align: center; left: 0px; background-color: rgba(0, 0, 0, 0); text-rendering: optimizespeed;" id="label2" class="design-mode-hidden">Noise Generations: </label><label style="margin: 0px; line-height: 1; overflow: hidden; overflow-wrap: break-word; max-width: 320px; border-style: solid; color: rgb(255, 255, 255); background-color: rgb(255, 164, 0); border-color: rgb(77, 87, 95); border-radius: 0px; border-width: 0px; font-family: &quot;Arial Black&quot;, Gadget, sans-serif; font-size: 18px; padding: 2px 15px; width: 320px; height: 25px; position: absolute; left: 0px; top: 275px; text-rendering: optimizespeed;" id="noiseGenerationsLabel">Noise Generations:</label><button id="newImageButton" style="padding: 0px; margin: 0px; border-style: solid; height: 30px; width: 100px; background-color: rgb(255, 164, 0); color: rgb(255, 255, 255); border-color: rgb(77, 87, 95); border-radius: 4px; border-width: 1px; font-family: Arial, Helvetica, sans-serif; font-size: 15px; position: absolute; left: 105px; top: 390px;">New Image</button><label style="margin: 0px; line-height: 1; overflow: hidden; overflow-wrap: break-word; max-width: 320px; border-style: solid; text-rendering: optimizespeed; color: rgb(255, 255, 255); background-color: rgba(0, 0, 0, 0); border-color: rgb(77, 87, 95); border-radius: 0px; border-width: 0px; font-family: &quot;Arial Black&quot;, Gadget, sans-serif; padding: 2px 15px; width: 255px; height: 155px; position: absolute; left: 25px; top: -1.66533e-16px; font-size: 25px; text-align: center;" id="loadingScreen" class="design-mode-hidden">Be patient! Noisy image loading!</label><img src="https://images.code.org/a43e09883806322c22831e46c24c7b9b-image18_708.jpg" data-canonical-image-url="https://images.code.org/a43e09883806322c22831e46c24c7b9b-image18_708.jpg" data-image-type="url" data-object-fit="contain" id="loadingImg" style="height: 145px; width: 140px; border-style: solid; border-width: 0px; border-color: rgb(0, 0, 0); border-radius: 0px; position: absolute; left: 85px; top: 125px; margin: 0px;" class="design-mode-hidden"><label style="margin: 0px; line-height: 1; overflow: hidden; overflow-wrap: break-word; max-width: 320px; border-style: solid; text-rendering: optimizespeed; color: rgb(255, 255, 255); background-color: rgba(0, 0, 0, 0); border-color: rgb(77, 87, 95); border-radius: 0px; border-width: 0px; font-family: &quot;Arial Black&quot;, Gadget, sans-serif; font-size: 28px; padding: 2px 15px; width: 145px; height: 30px; position: absolute; left: 80px; top: 90px; text-align: center;" id="percentLabel" class="design-mode-hidden">0%</label></div></div>
"""  # The provided sample input

result = extract_strings(html_input)
index = 0
tempStr = ""
tempStr += "var TRANSLATIONTEXT = {\n"
for (type, element_id, string) in result:
    tempStr += f'  "{element_id}_{index}": "{string}",\n'
    index += 1
tempStr = tempStr[:-2] + "\n"
tempStr += "};"
print(tempStr)
print()

library_name = "HAIWL5"

index = 0
for (type, element_id, string) in result:
    print(f'var {element_id}[property] = I18n_{library_name}.translate("{element_id}_{index}");')
    index += 1

# TODO: Check the type of the element, and use that to replace [property] (ie: label/button/textarea: Text, option: Option, etc)

# TODO: Generate the setText / setProperty statements based on the type. Tricky for dropdown options - need to create an array?