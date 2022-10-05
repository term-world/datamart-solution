
| Date              |          |
|:------------------|:---------|
| 3 October 2022 | Assigned |
| 16 October 2022    | Due      |
| Status            | [![GatorGrader](../../actions/workflows/main.yml/badge.svg)](../../actions/workflows/main.yml) |

# GLORIOUS NEW DATA PROJECT ON HORIZON! FUTURE OF `term-world` LOOKING BRIGHTER THAN EVER!

**Delivered by `Official Mayor-Endorsed News` on `5 October 2022`!**

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

## Accessing `datamart` Content

In order to complete the workload for the `datamart` you'll first need to `clone` the `datamart` repository into your `workshop`.

When you `clone` a repository you're duplicating its contents and adding them to your local workspace. Since you'll be working collaboratively with your neighbors, you'll each need your own copy of the `datamart` to work with.

In order to keep some of the magic (read: somewhat convoluted code) that makes `term-world` work the way it does, **you are required to clone all additional repositories within the `workshop`, located within your `garage`.**

Head to GitHub and:
* click on the green `Code` button
* ensure that `SSH` is selected
* copy the link that appears in the window below

It might look something like `git@github.com:term-world/ix-datamart`.

Once you've copied this link, navigate to your terminal window and ensure you're still in the appropriate place (in this case, the topmost level of your `workshop`). Then, enter the command:

```
git clone COPIED-LINK-HERE
```

Be sure to replace the fragment `COPIED-LINK-HERE` with the link you copied. In the example regarding `ix-datamart`, the full command would look like:

```
git clone git@github.com:term-world/ix-datamart
```

While `pull` is used to *update* the contents of a repository that already exists in your local workspace, `clone` is used to *replicate* the contents of a repository from GitHub and copy them to your local workspace.

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

### `builder`

#### `data_creator.py`

Leverges the `main` function to:

* Uses the `add_names` function to add a `list` of names to a newly-created `registry.csv` file

#### `table_builder.py`

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

Uses the following function (it is already written for you):

|Function name |Parameters  |Return type | Description                                               |
|:-------------|:-----------|:-----------|:----------------------------------------------------------|
|sorter        |`str`       |`None`      |Sorts column by given name (`str`) provided as parameter             |

Implements and uses the following function(s):

|Function name |Parameters*  |Return type | Description                                               |
|:-------------|:-----------|:-----------|:----------------------------------------------------------|
|switch_columns|`str`, `str`|`None`      |Retrieves and swaps two column with titles given as `str`             |

`*` The parameters for this function _can_ be `int`, `int`

### analyzer

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

## Branching `datamart` content

Even when working collaboratively with others on a single project, you'll still need to `add`, `commit`, and `push` your work. However, there's a few additional steps that have to be taken to keep your group's workflow organized.

Each repository has a `main` version of itself that represents exactly that, the "main" version of the repository. This is the version that is cloned whenever somebody runs a `git clone` command with that repository as its target, and the contents of `main` are what is pulled when somebody updates their local workspace's version of the repository with `git pull`.

However, each repository can also have multiple alternative versions of itself that simultaneously exist. These versions are referred to as "branches".

Branches are *very* useful when collaborating with other people on the same project--they can keep multiple portions of a developing project organized, and keep partially implemented (or incomplete) code from interfering with other developers.

You'll see firsthand just how useful this is as we work collaboratively over the next couple weeks, but for now, trust us: going through the extra couple of steps to branch your work when starting a new project (*especially* when working with other people) is a proactive step to avoiding many a headache later in the development process.

So, how do we do that?

First things first, navigate to the repository being worked on in your terminal window. For this content, that's the cloned `traffic-circle` in your `workshop`.

Then, run the following command:

```
git checkout -b FEATURE
```

Just be sure to replace the `FEATURE` fragment with a name that succinctly describes the work you're contributing to the overall project. (You might also consider including your username within the branch name if you think it'll help your group stay organized.) For instance, if the user `dluman` and someone else are working on the `east` folders' `Stoplight.py`, `traffic-circle`, he might run the command:

```
git checkout -b table-analyzer
```

**Whenever you're starting your work, you should always `git pull` from any branches you're using in tandem with _other folks_. This guarantees that you solve content issues early and _often_.**

## Evaluating `datamart` Content

In order to run the `grader` for this week's work, you'll need to be in the topmost level of the `datamart` folder (which should have been cloned within the `workshop`). Once there, run the command:

```
gatorgrade
```

### Making an improvement proposal

This assignment begins your opportunity to propose and improve the world of `term-world` at-large. For this assignment, proposals may include making graphics to improve the `bodega` site experience, creating new items or actions in the `traffic-circle` itself or another assignment-related improvement not contemplated in the prior narrow categories.

To make an improvement proposal, you must _create an issue_ on this repository. Do so by:

* clicking the `Issues` tab at the top of the page.
* clicking the green `New Issue` button
* selecting the `Improvement Proposal` template 

**You must fill out the entire template and wait for Mayoral approval before starting the improvement.**

#### Improvement suggestions

The functionality for the `datamart` is pretty basic. You probably will get frustrated when you're adding things to columns,
and the program takes _forever_ to add to all of the rows (you have to do it 1-by-1, as you'll find out). Suggestions for improvements for this work are a bit easier to come up with, such as:

* Adding a list of values as a column (rather than 1-by-1)
* Deleting an entire column
* Searching for a list of words rather than just `1` at a time
* Searching a specific column for a value (rather than the whole table)

This list is not meant to be exhaustive. It's possible that you'll come up with a few more unique to your neighborhood. When you have an idea, _file the issue_ and get to work!

## Submitting `datamart` Content

Considering that the work you're doing for the `bodega` will be in a particular `branch` of the repository, there's a small adjustment that has to be made to our normal `add`, `commit`, `push` process.

When you're ready to push to GitHub, do the normal `add` and `commit` routines. Recall:

```
git add -A
```

```
git commit -m "Descriptive commit message"
```

### Pushing to a branch

However, when it comes to push, run this slightly expanded command:

```
git push origin YOUR_BRANCH_NAME
```

We're still using `git push`, but this time we're adding an extra layer of information to the command; to be precise, we're specifically instructing `git` to push our changes to a particular branch of the repository (*your* branch). In the example regarding the `bodega_cat`, the command to run would look like:

```
git push origin east-stoplight
```

### A "Pull Request"

Once you've completed this step, you'll now need to create a **pull request** on GitHub. This is a formal request to other collaborators on your project to review the code you've submitted--an important step when working together on the same project.

In a web browser, navigate to the repository page on GitHub (for the repository that you've just submitted new changes for). Towards the upper-left corner you'll see a dropdown that will have `main` selected as default (`main` being one of the branches for your repository, this is the "production-ready" branch). Select your branch from the dropdown, and you may see a yellow box prompting you to create a pull request; click that if you see it, or navigate to `Pull Requests` at the top and subsequently click the green `New pull request` button.

Now, in the top left corner select the branch you wish to add your updated changes to, or the "base" branch--generally speaking this will likely be `main`, the aforementioned "production-ready" branch. In the bar on the righthand side, add Reviewers to the pull request (this should be all of your neighborhood collaborators). Finally, click `Create pull request`.

You'll also be responsible for responding to and reviewing pull requests created by other collaborators on your team. Comment on each other's work about changes you'd like to see made to code submitted, and be sure to keep all communication both specific and professional.

## Merging `datamart` Content on GitHub

After all collaborators have had a chance to weigh in on a new pull request, if the work is up to snuff and ready to join the "production-ready" `main` branch, then your designated neighborhood team lead will have to merge that work into the `main` branch.

If you *are* said team lead, you'll need to navigate to the pull request on GitHub. If there are no "conflicts" (i.e., differences that can't be automatically handled by GitHub) between the pull request's branch and the `main` branch, simply click the `Commit merge` button and the merge is complete!

In some cases however, you'll have to specify what parts of a pull request make it into the `main` branch. If that's the case, you'll instead see a `Resolve conflicts` button. Click that and you'll be presented with a proposed merged copy of the code, with some extra lines added in. Something akin to:

```
<<<<<<
x = "this_is_a_line_of_code"
=======
x = "this_is_a_different_line_of_code"
>>>>>>
```

To resolve said conflicts, you'll need to delete the portion of code you don't want to appear in the final product, as well as any `<<<<<<`, `======`, or `>>>>>>` lines.

Once complete, click `Mark as resolved` followed by `Commit merge`, and the changes on the branch will be joined with the `main` branch!

## Updating `datamart` Content in Your Local Workspace

At some point you may wish to update the content in your local workspace with the changes being implemented by your teammates. 

To do so, `git checkout main` (or other collaborative branch) and run the command:

```
git pull
```

This will update your local workspace with the content stored in the `main` branch.

### `checkout` other folks' branches

It's _very_ likely that you'll run into the need to `checkout` a branch that GitHub has, but you don't. Here's a reminder of the steps to do that.

First, `fetch` all of the changes from the `remote` (GitHub):

```
git fetch --all
```

Once you've received this information, to `checkout` the `east-stoplight` branch (for example):

```
git checkout --track origin/table-analyzer
```

This will copy that branch from GitHub to your local workspace. You'll now also be able to `push` and `pull` to/from it.