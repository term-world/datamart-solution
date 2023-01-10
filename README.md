
| Date              |          |
|:------------------|:---------|
| Todo | Assigned |
| Todo    | Due      |
| Status            | [![GatorGrader](../../actions/workflows/main.yml/badge.svg)](../../actions/workflows/main.yml) |

# GLORIOUS NEW DATA PROJECT ON HORIZON! FUTURE OF `term-world` LOOKING BRIGHTER THAN EVER!

**Reported by `Official Mayor-Endorsed News` on `Tdoo`**

Welcome to the inaugural report from `Official Mayor-Endorsed News`!
Given the recent defunding and dissolution of TNN following last week's
egregious journalistic debacle involving what our Mayor calls "fake
news", the `Official Mayor-Endorsed News` is here to ensure all the
fair citizens of `term-world` stay informed of the exciting new
developments our Mayor has in store for our community!

And boy do we have some exciting news to share regarding one of the most
ambitious projects to be proposed by our Mayor! But why take our word
for it, when you could hear about this new endeavor directly from our
Mayor! In an exclusive interview with `Official Mayor-Endorsed News`,
our Mayor had the below information to share!

"Your Mayor here with a new proposal sure to inspire you all to new
levels of greatness! I've recently learned that this thing called 'Big
Data' is *all* the talk outside `term-world`, and I--your Mayor--am
here to say it's time we brought it to our incredible community!"

The newly constructed `datamart` will house *all* manner of data science
projects meant to collect and synthesize the latest data on the fair
citizens of `term-world`! As per usual, our Mayor is counting on *YOU*
to help his vision of a `term-world` up-to-date with all the latest
"Big Data" trends become a reality!

## Overview

In this set of activities we cover:

* working collaboratively using Github
* branching
* merging
* issuing "Pull Requests"
* exploring `data structures`, namely `list`s, a Python feature which:
  * allows storage of many values in one variable
  * organizes itself by _indexes_ (that is, numerical "addresses")
  * is _mutable_, which means it can expand or contract
* `method`s: features of Python objects which act like "powers" of a given _kind_ of object

You'll complete several main tasks:

* collecting and entering data from various neighborhoods
* organizing and rearranging that data
* doing basic data analysis on that data

### Supporting media

[![YouTube thumbnail](http://img.youtube.com/vi/4eapZtdVpDM/hqdefault.jpg)](https://youtube.com/playlist?list=PLJvBsjwXNdlFZ377qYXa76_1c-WXTuhA5)

## Completing `datamart` content

The `datamart` is composed of three distinct pieces, sorted into folders:

1. The `builder/data_creator.py` and `builder/table_builder.py` files which create and edit the data
  * The `builder/data_creator.py` file should be completed and run _first_; all other files depend on its output
2. The `arranger/table_arranger.py` file 
  * sorts columns, reorganizes (i.e. switches) column layout
3. `analyzer/table_analyzer.py` file
  * Performs basic analysis on the data including:
    * averaging columns
    * finding the maximum value
    * counts the occurences of a given search term across _the whole table_

As written above, **finish the `data_creator.py`** file first, as file storing the data isn't created until 
we run the creator program and provide inputs.

Requirements for each file are enumerated below. However, a general note:

> To solve each after the `data_creator.py`, we need to handle the `menu` options that appear on the screen. 
> This will require a set of `if` statements to test the outcome of the `menu` function and determine which
> number was chosen from the menu

#### Note

These programs use two `global` variables to house the data in the table and the names of columns. Use:

|Variable |Purpose |
|:--------|:-------|
|DATA†     |Holds data from table |
|COLS††     |Holds names of columns |

`†` This is a `list` of `list`s -- so, be careful
`††` The columns list is _always_ the first list/row

### `builder`

#### `data_creator.py`

Collects the names of individual residents of various neighborhoods.

Leverges the `main` function to:

* Creates a blank list to hold user names input to program
* Uses the `add_names` function to add a `list` of names to a newly-created `registry.csv` file

#### `table_builder.py`

Adds additional columns to data to complete the data set.

Implements and uses the following functions:

|Function name |Parameters  |Return type | Description                                               |
|:-------------|:-----------|:-----------|:----------------------------------------------------------|
|get_row       |`int`       |`list`      |Returns a chosen row of the table as a list                |
|add_column    |`str`       |`bool`      |Accepts a string name for column; returns `True` if successful |
|add_to_row†   |`int`, `str`|`bool`      |Accepts a row number and a string of data to add to that row; returns `True` if successful |
|remove_from_row†† |`int`      |`bool`      |Accepts a row number from which to delete the last entry; returns `True` if successful |

`†` This function always adds to the end of a row

`††` This function always removes the _last_ entry in a row

To complete this part of the assignment, each member of your team needs to develop `3` questions to ask other tables to gather
data on their activities pertaining to work they've completed for class. This could be something like (but not limited to):

* number of commits on the `bodega` and `traffic-circle` assignments
* number of Pull Requests opened and closed on the above-named assignments
* number of neighborhood members

Asking for all names of neighborhood members is _required_ and does not count toward your `3` question total. When developing questions, think broadly about all of the data that you think is of interest re: your fellow citizens' work in `term-world`.

It's not like we're collecting this for any _reason_, you know.

Each neighborhood is responsible for gathering data from all other tables in a relatively quick and efficient manner. Most teams will send out 5 representatives to ask questions. Remaining team members should begin to solve `data_creator.py` so that the tool can be made available to neighborhood members.

### `arranger`

#### `table_arranger.py`

Allows us to rearrange the table to suit various data analysis needs.

Uses the following function (it is already written for you):

|Function name |Parameters  |Return type | Description                                               |
|:-------------|:-----------|:-----------|:----------------------------------------------------------|
|sorter        |`str`       |`None`      |Sorts column by given name (`str`) provided as parameter             |

Implements and uses the following function(s):

|Function name |Parameters*  |Return type | Description                                               |
|:-------------|:-----------|:-----------|:----------------------------------------------------------|
|switch_columns|`str`, `str`|`None`      |Retrieves and swaps two column with titles given as `str`             |

`*` The parameters for this function _can_ be `int`, `int`

##### Note

This must rearrange the table such that `ID` comes first, followed by `Neighborhood`, then `Name`. Any other rearranging
you do is extra (though it might be helpful when looking at the data).

In addition, you must sort the table by Neighborhood name when finished with the assignment.

### analyzer

Leverages some basic analysis to tell us facts about facts (metadata) about neighborhoods.

Once all data has been collected and entered for all respondents, neighborhoods should complete the `table_analyzer.py` file, implementing and using:

|Function name |Parameters*  |Return type | Description                                               |
|:-------------|:-----------|:-----------|:----------------------------------------------------------|
|counter|`str`|`int`      |Counts instances of the `str` entered as a parameter, returns count of that `str`            |
|avg_column| `str` | `float` |Takes the column name as a parameter and averages the contents of that column |
|max_value|`str`|`any`|Takes column name as parameter and finds the maximum value in that column |

`*` The parameters for these functions _can_ be `int`

Your [reflection](office/reflection.md) should report the outcomes of these operations.

### Collaborative reflection

**Create one branch called `reflection` to capture your work on this section of the assignment; all members should contribute to the same branch.**

All of the above tasks completed, finish the collaborative reflection located in the `office`.

## Making an improvement proposal

This assignment begins your opportunity to propose and improve the world of `term-world` at-large. For this assignment, proposals may include making graphics to improve the `bodega` site experience, creating new items or actions in the `traffic-circle` itself or another assignment-related improvement not contemplated in the prior narrow categories.

To make an improvement proposal, you must _create an issue_ on this repository. Do so by:

* clicking the `Issues` tab at the top of the page.
* clicking the green `New Issue` button
* selecting the `Improvement Proposal` template 

**You must fill out the entire template and wait for Mayoral approval before starting the improvement.**

#### Improvement suggestions

The functionality for the `datamart` is pretty basic. You probably will get frustrated when you're adding things to columns,
and the program takes _forever_ to add to all of the rows (you have to do it 1-by-1, as you'll find out). Suggestions for improvements for this work are a bit easier to come up with, such as:

|Improvement Suggestions |Description        |Example(s)         |
|:--------------------|:------------------|:----------|
|Adding lists            |Adding a list of values as a column (rather than 1-by-1)     |      |
|Deleting column              |Adding a functionality that deletes an entire column    |      |
|Searching for words     |Searching for a list of words rather than just `1` at a time    |      |
|Searching a column                |Searching a specific column for a value (rather than the whole table)    |      |
|Sorting information                |Sorting by more than one column at a time     |      |
|Deleting names                |Deleting a name in `data_creator.py` for it to no longer exist in the `registry.csv`     | Look into the `table_builder.py`     |
|                |     |      |
|                |     |      |
|                |     |      |
|                |     |      |

This list is not meant to be exhaustive. It's possible that you'll come up with a few more unique to your neighborhood. When you have an idea, _file the issue_ and get to work!

## Backup Policy Reminder

**While we may use this server to store code, you are responsible for using GitHub as your main backup.**

In the event that the `term-world` server goes down for any unforeseen reason, your work may be lost. Though this server is backed up on a regular (i.e. weekly) basis, there is no guarantee that up-to-the-minute data for your work will be restored.

Remember: to err is human; to back up your work is *divine*.
