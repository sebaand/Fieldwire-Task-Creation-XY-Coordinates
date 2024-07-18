This is program is designed to scrape unflatted pdf drawings for specific call outs as per a refernce file selected by the user.
The program searches for those call outs in the pdf and calculates the X - Y position of the call outs with respect to the 
page, and then outputs the corresponding values into a .csv which can be copied directly into the task importer in fieldwire.

Information for proper use:
- Reference call out file must be a single column .csv file. Note it assume the column has a title in cell A1, so it will ignore the first cell of the column.
- The shop drawings file must be an unflatted .pdf file. 
- It skips the first page as it assumes a front page and any matches there with the reference file don't actually require a task.
- It ignores any match within the bottom right corner of the sheet as it assumes that's the title block section of the sheet and doesn't actually require a task.
- Currently the plan name that is automatically generated is in the format {file_name} - {page number}. Optimal workflow assumes you first upload the pdf file to fieldwire and revert to page number for the filename when importing the plans. Then you import the tasks by copying the content of the output excel file into the import tasks tab of fieldwire. After having imported the tasks you can scan the title blocks. 
- Note that the import tasks tab of Fieldwire is limited to import 500 tasks at a time, so if you have more than 500 tasks to import you must do so in multiple separate imports.

Any questions please feel free to reach out to the your hilti representative.  Note this program is not an official Hilti product and is offered as a contribution to the open-source community and neither the author nor the Hilti Group and it's affiliated companies assume any liabilty associated to the output of the code or any associated use. 

Also a special thanks to <a href='https://pngtree.com/so/Initial'>Initial png from pngtree.com/</a> for providing the png 
for the executable icon. 
