This is program is designed to scrape shop drawings for specific call outs as per a refernce file selected by the user.
The program searches for those call outs in the pdf and calcualtes the X - Y position of the call outs with respect to the 
page, and then outputs the corresponding values into a .csv which can be copied directly into the task importer in Fieldwire.

Instructions for the user:
- Reference Call out file must be a single column .csv file which contains all the callouts that you want an associated task for in Fieldwire.
- The shop drawings file must be an unflatted .pdf file. 
- The current executable skips the first page as it assumes that the front page  requires no associated tasks.
- The current executable doesn't extract information for the bottom right corner of the page, as it assumes that's the location of the title block.

Also a special thanks to https://pngtree.com/freepng/initial-letter-xy-logo-template-design_3579444.html for providing the png 
for the executable. 