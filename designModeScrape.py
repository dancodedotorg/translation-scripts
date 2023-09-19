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
<div id="designModeViz" class="appModern clip-content" tabindex="1" data-radium="true" style="width: 320px; height: 450px; transform: scale(0.81875);"><div class="screen" tabindex="1" data-theme="default" id="screen1" style="display: block; height: 450px; width: 320px; left: 0px; top: 0px; position: absolute; z-index: 0; background-color: rgb(255, 255, 255);"><label style="margin: 0px; line-height: 1; overflow: hidden; overflow-wrap: break-word; max-width: 320px; border-style: solid; text-rendering: optimizespeed; color: rgb(77, 87, 95); background-color: rgba(0, 0, 0, 0); border-color: rgb(77, 87, 95); border-radius: 0px; border-width: 0px; font-family: &quot;Arial Black&quot;, Gadget, sans-serif; font-size: 13px; padding: 2px 15px; width: 240px; height: 60px; position: absolute; left: 35px; top: 125px;" id="label1">Pick a color!</label><select id="dropdown1" style="width: 200px; height: 30px; margin: 0px; border-style: solid; background-color: rgb(255, 255, 255); color: rgb(77, 87, 95); background-image: url(&quot;data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%20256%20448%22%20enable-background%3D%22new%200%200%20256%20448%22%3E%3Cstyle%20type%3D%22text%2Fcss%22%3E.arrow%7Bfill%3A%234d575f%3B%7D%3C%2Fstyle%3E%3Cpath%20class%3D%22arrow%22%20d%3D%22M255.9%20168c0-4.2-1.6-7.9-4.8-11.2-3.2-3.2-6.9-4.8-11.2-4.8H16c-4.2%200-7.9%201.6-11.2%204.8S0%20163.8%200%20168c0%204.4%201.6%208.2%204.8%2011.4l112%20112c3.1%203.1%206.8%204.6%2011.2%204.6%204.4%200%208.2-1.5%2011.4-4.6l112-112c3-3.2%204.5-7%204.5-11.4z%22%2F%3E%3C%2Fsvg%3E&quot;); border-color: rgb(0, 0, 0); border-radius: 4px; border-width: 1px; font-family: Arial, Helvetica, sans-serif; font-size: 13px; padding: 0px 30px 0px 15px; position: absolute; left: 60px; top: 200px;"><option>Red</option><option>Blue</option></select><button id="showChoice" style="padding: 0px; margin: 0px; border-style: solid; height: 40px; width: 150px; background-color: rgb(255, 164, 0); color: rgb(255, 255, 255); border-color: rgb(77, 87, 95); border-radius: 4px; border-width: 1px; font-family: &quot;Arial Black&quot;, Gadget, sans-serif; font-size: 15px; position: absolute; left: 75px; top: 310px;">See my choice</button><input id="text_input1" style="margin: 0px; width: 200px; height: 30px; border-style: solid; color: rgb(77, 87, 95); background-color: rgb(242, 242, 242); border-color: rgb(77, 87, 95); border-radius: 4px; border-width: 1px; font-family: Arial, Helvetica, sans-serif; font-size: 13px; padding: 5px 15px; position: absolute; left: 60px; top: 25px;" placeholder="placeholderTest"><div contenteditable="true" class="textArea" id="text_area1" style="width: 200px; height: 100px; border-style: solid; background-color: rgb(242, 242, 242); color: rgb(77, 87, 95); border-color: rgb(255, 255, 255); border-radius: 2px; border-width: 1px; font-family: Arial, Helvetica, sans-serif; font-size: 13px; padding: 5px 15px; position: absolute; left: 60px; top: 350px; margin: 0px;">divTest</div></div></div>
"""  # The provided sample input

result = extract_strings(html_input)
index = 0
tempStr = ""
tempStr += "var TRANSLATETEXT = {\n"
for (type, element_id, string) in result:
    tempStr += f'\t"{element_id}_{index}": "{string}"\n'
    index += 1
tempStr += "}"
print(tempStr)
print()

library_name = "HAIW"

index = 0
for (type, element_id, string) in result:
    print(f'var {element_id}[property] = I18n_{library_name}.translate("{element_id}_{index}")')
    index += 1