
import PySimpleGUI as sg

feet_label = sg.Text("Enter feet: ")
inches_label = sg.Text("Enter inches: ")
feet_input = sg.InputText(key="feet")
inches_input = sg.InputText(key="inches")
convert = sg.Button("Convert")
result = sg.Text("",key="result")
window = sg.Window("Converter",layout=[[feet_label,feet_input],
                                       [inches_label,inches_input],
                                       [convert,result]],
                   font=("Helvetica",16))





while True:
    event,values = window.read()
    match event:
        case "Convert":
            final_re=round((float(values["feet"])*0.3048 + (float(values["inches"])*0.0254)),3)

            window["result"].update(value=f"{final_re} m",
                                    text_color="white")
        
        case sg.WIN_CLOSED:
            break

    
window.close()