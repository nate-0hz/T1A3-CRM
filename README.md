# Nathan Picone - T1A3 - Terminal Application Assignment

## Referenced Sources

## Source Control Repository Link

GitHub - https://github.com/nate-0hz/T1A3-CRM

## Video Presentation link

Youtube - https://www.youtube.com/watch?v=VZF4nuslFag

## Style guide

[Python pep8](https://peps.python.org/pep-0008/) is the style guide used. Particular attention has been paid to:

### Indentation
[Appropriate indentation for 4 spaces](https://peps.python.org/pep-0008/#indentation)
[Maximum line length of 79 spaces](https://peps.python.org/pep-0008/#maximum-line-length)
[Breaking appropriately around binary operators](https://peps.python.org/pep-0008/#should-a-line-break-before-or-after-a-binary-operator)
[Blank lines areound classes and elsewhere](https://peps.python.org/pep-0008/#blank-lines)
[Importing on separate lines](https://peps.python.org/pep-0008/#imports)
[The appropriate use of whitespace in expressions and statements](https://peps.python.org/pep-0008/#whitespace-in-expressions-and-statements)


## Application features

The application is the beginnings of a Contact Relationship Manager (CRM), and holds basic information about the contacts held within, including:

* First and last name
* Phone number
* Company
* Email address
* Contact’s birthday
* Date the person was last contacted (manually updatable by the user)
* Date the user wishes to contact the person next (manually updatable)

The application has several features:

* Main menu
* Automatic creation of the storage csv, if it does not exist
* View Records flow
* Ability to sort and display records, by attribute
* Ability to search records for partial strings and numbers
* Ability to filter out duplicate returns, when searching
* Add Records flow
  * Ability to exit the adding of a record
  * An in-built check if the entered name already exists, giving the user the choice of adding the record or skipping
  * Saving the added record to the storage csv file
* Edit Record flow
  * Ability to search for and select the record to be edited
  * Ability to update or skip updating individual fields within the record
* Contextual help from text files on several menus

### Main Menu

The application has a main menu, which is presented when the application is launched.

The Main Menu holds selectable options to initiate the chosen flows, ability to display a simple contextual help text file, and the ability to quit the application gracefully.

![main-menu-01](https://github.com/nate-0hz/T1A3-CRM/assets/33781520/ba8e8dd1-9a1c-4203-adfc-19a91aa38c96)

![Main_menu drawio](https://github.com/nate-0hz/T1A3-CRM/assets/33781520/04693055-d4c6-49ca-aa17-4403249b6f91)


### Automatic creation of storage csv file

On launching the application, a check is performed to determine if the storage csv file exists. If it does not, the file is automatically created, preventing any issues saving new records the user creates.

This also makes it possible to ship the application with sample data, as the user can try using the application with sample data, then delete it, prior to building their own database of records.

It does this through a try/except block for FileNotFoundError. If cram_storage.csv is not found in the /data_files folder, a csv of the same name is created, with full column headers but no data.

### View Records

This feature allows the user to choose between viewing all stored records, sorted by attribute, selectable by the user, or to search for specific records.

![view-menu-1](https://github.com/nate-0hz/T1A3-CRM/assets/33781520/1a17292f-683a-40db-8546-662a1f0a1b59)


Viewing all records uses Pandas to create a data frame from the storage csv file, the sorts the data frame in ascending order, on the column of the user’s choosing.

![View-flow drawio](https://github.com/nate-0hz/T1A3-CRM/assets/33781520/527559f9-3f8a-4cb2-b409-2915aba492a5)


### Sort Records

On selecting View All Records, the user is presented with a menu of sort by options to choose from.

![view-menu-2](https://github.com/nate-0hz/T1A3-CRM/assets/33781520/37a2878e-b34d-44c2-b419-b076b7406f24)


Selecting from these options will display the entire database, in ascending order, on the attribute chosen.

![view-menu-3](https://github.com/nate-0hz/T1A3-CRM/assets/33781520/567d049c-269f-4439-a415-54b7e110fafb)

On pressing enter, the user will return to the View Contacts Menu

### Search Records

Searching for records using a substring is a little more complicated. This also uses pandas to create a data frame. The substring is changed to accommodate multiple capitalisation variations, and is tested against each value in each row of the data frame, and if a match is found, the entire row is copied to temporary storage in a second csv file. Once all rows of the data frame have been searched for the substring, the application then examines the second csv for duplicate rows, and drops them, as it writes the rows to a third csv file.

When complete, the cleansed data is moved from the third csv file into a new data frame and displayed for the user.

![view-menu-4](https://github.com/nate-0hz/T1A3-CRM/assets/33781520/4105c41e-b3d5-45dc-84c8-68e8a0630de8)

![view-menu-5](https://github.com/nate-0hz/T1A3-CRM/assets/33781520/ed3e483c-d37a-441a-8b5b-df40181f102d)


### Search Records - Duplicate cleansing

Once the search flow is initiated, the temporary storage csv has any data it might be holding deleted, and the column headers are returned to the empty file.

As the search string can be very generic, duplicate entries are often found, where the same pattern for letters or numbers can be found in the same record:

![view-menu-6](https://github.com/nate-0hz/T1A3-CRM/assets/33781520/761cf85c-a256-4b99-8635-e5b4a3f8e40d)

This application handles this by dropping duplicate rows as it moves the files to the third “clean” csv file

![view-menu-7](https://github.com/nate-0hz/T1A3-CRM/assets/33781520/a225cefa-d64e-4736-8093-9ce82feca82d)


These results are moved to a data frame through Pandas, and displayed to the user, in the same order they can be found in the main storage csv.

### Add Record and check if name exists

Adding a contact triggers the input prompt asking the user to enter the first name of the person they wish to add. At this point, the user can type “exit” to go back to the main menu.

![add-menu-1](https://github.com/nate-0hz/T1A3-CRM/assets/33781520/87a6e1b9-cddc-479f-9086-d2fbec65d3fe)


The application then asks for the person’s last name, then performs a check whether the first and last names entered already exist in the main storage csv. If they do, the user is given the option to continue or not. Not continuing returns the user to the main menu.

![add-menu-2](https://github.com/nate-0hz/T1A3-CRM/assets/33781520/fabb739b-3df9-4289-a3d5-516048c736b4)

If the user elects to continue, they can keep entering details until all fields have been completed. The user can press enter to leave a field blank.

On completion, the user is returned to the beginning of the add loop where they can add another user or type “exit” to exit. Continuing straight on, without giving the user an option to continue or end is faster and more convenient if adding multiple entries.

![add-menu-3](https://github.com/nate-0hz/T1A3-CRM/assets/33781520/9592c82d-94e5-4266-983b-fca107f50ff5)

![Add-flow drawio](https://github.com/nate-0hz/T1A3-CRM/assets/33781520/c0b47a97-c690-4963-b9a4-b9b24d49c010)

### Edit Record

On editing a record, the user is presented with an input prompt, to enter a substring to search for.

![edit-menu-1](https://github.com/nate-0hz/T1A3-CRM/assets/33781520/4d969ad3-c5e3-4f16-bbc8-2e4cec54be03)


On pressing enter, much of the view search functionality is performed here, with the substring being searched for in a data frame of all entries, and matched entries being cleansed of duplicates, then presented to the user for selection.

![edit-menu-2](https://github.com/nate-0hz/T1A3-CRM/assets/33781520/550c08ee-a9ad-4129-950d-2dc1b0d2d3fa)

The user is then asked to input which record they would like to edit, be selecting the index number on the table’s left.

When selected, that row is converted to a list (chosen_record), containing the current values, and a dictionary (editing_dict) containing the current keys and values, along with an empty list (temp_list).

The dictionary is used to guide the user to make the changes, one at a time, stepping out the key and value, and giving the user the option to press ‘enter’ to keep the current value.

![edit-menu-3](https://github.com/nate-0hz/T1A3-CRM/assets/33781520/3df9c02f-fdfe-4557-aa71-cba76fb6ea3b)

This process also sets and increments the index number for temp_list. If the user selects to keep the value of the key the same, the application adds the value from chosen_record to temp_list in the correct index position. If the user provides a new value, the new value is written to temp_list in the correct position index.

Once all values have been iterated through, the application finds the original row in the data frame and overwrites it with chosen_record. The user is then returned to the main menu.

![Edit-flow drawio](https://github.com/nate-0hz/T1A3-CRM/assets/33781520/6f5b6360-a91c-4de9-a493-cf7bd1f6c95f)


### Contextual Help

Contextual help can be accessed by pressing 9 from relevant menus. A simple class has been created for help, and instances of the class have been created to display the relevant help file in the terminal.

![help-1](https://github.com/nate-0hz/T1A3-CRM/assets/33781520/e81c6ca3-7276-468c-b18a-b8206ae4f538)


## Implementation Plan

The implementation plan was to design the flow, illustrated in the previous section, the implement the build, one section at a time, starting with the main menu.

I then planned to build the Add flow, View flow, Edit flow and Help flows as stand-alone applications that would then be called off the main menu.

As development progressed, and DRY was applied, it became clear that some functions and variables should be held in a separate file, so that they could be called upon by different flows. Relocating some functions and variables to the shared_variables.py file also improved readability of each flow.

To set out the implementation plan and track its progress, I used ClickUp, and rather than a checklist, I used subtasks. This also helped me remember to complete things I thought of when working on other tasks.

Sadly, I do not have images during development as one of the tasks I forgot to add was to take images during development, to demonstrate the use of the software during the project.

![implementation-plan-1](https://github.com/nate-0hz/T1A3-CRM/assets/33781520/7cf702d1-ec50-4e84-8078-1e2c9ab79ff4)

![implementation-plan-2](https://github.com/nate-0hz/T1A3-CRM/assets/33781520/77aa4756-d26c-4b35-bce4-634f95ff2b4f)

![implementation-plan-3](https://github.com/nate-0hz/T1A3-CRM/assets/33781520/1935f9aa-0be7-4740-b26e-635c172727cb)

![implementation-plan-4](https://github.com/nate-0hz/T1A3-CRM/assets/33781520/e5fe6405-dbdb-488d-afe3-07bd566e03f3)

![implementation-plan-5](https://github.com/nate-0hz/T1A3-CRM/assets/33781520/cbb3a142-8be2-411f-932c-b8f49585d1d1)

![implementation-plan-6](https://github.com/nate-0hz/T1A3-CRM/assets/33781520/c78bd31e-4630-400a-8c5e-826a40016e2e)

## Help Documentation

### Installing CRaM

Save the repository file to your hard drive.

In a terminal window, navigate to the save location folder.

Type `sh run.sh`

### Dependencies
All depedencies should be installed by the `run.sh` shell script.

For clarity, the following dependency was required to be installed by the developer, for the application to run correctly:
* Pandas

The application was tested on an M2 MacBook Pro with 16 GB shared memory and 1 TB hard drive, running MacOS Ventura 13.3.1 (a). The Python version used was Python 3.11.3. You may have issues running it on an older verion of Python 3.

Please note, it has not been tested on Python 2.

The other depencies were either installed by pandas or other packages.

Ensure you have dependencies listed in requirements.txt, but note that pyobjc-framework dependencies need some clean up.
