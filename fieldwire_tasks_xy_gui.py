import fitz  # PyMuPDF library
import pandas as pd
import PySimpleGUI as sg #library for the gui.
import os
import time

# Define the layout of the GUI
layout = [
    [sg.Text('Call Outs Reference List:'), sg.InputText(key='-FILE1-'), sg.FileBrowse(),sg.T('?', key='-CO_QUESTION_MARK-', tooltip='This file must be .csv file with 1 column only listing the call-outs to pin on your shop drawings.', enable_events=True, click_submits=False)],
    [sg.Text('Shop Drawings File:'), sg.InputText(key='-FILE2-'), sg.FileBrowse(),sg.T('?', key='-SHOP_QUESTION_MARK-', tooltip='Select the unflattened .pdf file of your shop drawings which you want to create tasks for in Fieldwire.', enable_events=True, click_submits=False)],
    [sg.Text('Select Output Directory:'), sg.InputText(key='-OUTPUTDIR-'), sg.FolderBrowse(),sg.T('?', key='-DIR_QUESTION_MARK-', tooltip='Select the output directory where to save your X_Y positions extract.', enable_events=True, click_submits=False)],
    [sg.Button('Run')],
    [sg.Text('', key='-OUTPUT-')] 
]

# Create the window from the layout
window = sg.Window('File Selection', layout)
# Define the column headers as a list which matches the fieldwire import tasks table
column_headers = ['Title','Status','Category','Assignee email','Start date','End date','Plan','X pos(%)','Y pos(%)']

# Event loop to process events and get input from the GUI
while True:
    event, values = window.read()
    # If the window is closed or 'Run' button is clicked, exit the loop
    if event == sg.WINDOW_CLOSED:
        break
        
    file1_path = values['-FILE1-']
    file2_path = values['-FILE2-']
    output_dir = values['-OUTPUTDIR-']

    # Update the input fields with the selected file/directory paths
    if event == 'Browse':
        window[event].update(values[event])
        # Get the selected file and directory paths

    if event == 'Run':
        try:
            Ref_df = pd.read_csv(file1_path, encoding='latin-1') # Load the CSV file into a DataFrame
            Output_df = pd.DataFrame(columns=column_headers) # crea

            # open the document
            doc = fitz.open(file2_path)

            # creating empty lists to host the dataframe series for later
            name = [] 
            x_pos = []
            y_pos = []
            sheet = []
            filename = os.path.basename(doc.name)
            filename = filename.strip(".pdf")
            for page in doc:    #iterate page by page across the shop drawing
                width, height = page.rect.width, page.rect.height # get the page size
                page_nm = int(str(page).split(" ")[1].split(" ")[0])+1 #stripping the fitz.page type of all the info except the page number and adding 1 get correct number
                print(page_nm, width, height)
                window['-OUTPUT-'].update(f'Computing X-Y Locations of page {page_nm}')
                window.refresh() # Force immediate GUI window update
                if page_nm > 1: # >1 skips the front page as don't want to create any tasks there
                    for system in Ref_df.iloc[:, 0]:
                        text_instances = page.search_for(system)
                        for i, inst in enumerate(text_instances):
                            x = round(((inst.x0 / width)+(inst.x1 / width))*50,0) # normalize coordinates by dividing by width and height
                            y = round(((inst.y0 / height)+(inst.y1 / height))*50,0)
                            if x > 77 and y > 85: #using if statement to remove matching text that is in the titlte block section of the drawing
                                pass
                            else:
                                name.append(pd.Series(f"{system}_{i}"))
                                x_pos.append(pd.Series(x))
                                y_pos.append(pd.Series(y))
                                sheet.append(pd.Series(f"{filename} - {page_nm}"))
                else:
                    pass
            Output_df['Title'] = pd.concat(name, ignore_index=True) #add the calculated locations to the output dataframe
            Output_df['Plan'] = pd.concat(sheet, ignore_index=True)
            Output_df['X pos(%)'] = pd.concat(x_pos, ignore_index=True)
            Output_df['Y pos(%)'] = pd.concat(y_pos, ignore_index=True)

            output_file = f"{output_dir}/{filename}_Penetrations X-Y Location.csv"
            Output_df.to_csv(output_file, index=False) #generate a csv from the analysis dataframe
            window['-OUTPUT-'].update('Computation Complete, Whoop!')
            window.refresh()
            time.sleep(2)
            window['-OUTPUT-'].update('')
            window.refresh()
            break
        except:
            window['-OUTPUT-'].update('Something went wrong')
            window.refresh()
            time.sleep(2)
            window['-OUTPUT-'].update('')
            window.refresh()
window.close()


