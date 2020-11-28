# [Advent of Code 2020](https://adventofcode.com/) - Mathis Group
⁣    🌟  
    🎄  
   🎄🎄  
  🎄🎄🎄  
 🎄🎄🎄🎄  
🎄🎄🎄🎄🎄  
  🎁🎁🎁
  
The solutions are automatically tested with github-actions.

[![Build Status](https://github.com/vidalmaxime/adventofcode-2020/workflows/CI/badge.svg)](https://github.com/vidalmaxime/adventofcode-2020/actions?query=branch%3Amaster)


## Install requirements
After creating a conda/virtualenv environment, run
```bash
pip install -r requirements.txt
```
## Usage

Use `./aoc` script

```
usage: aoc <command> [<args>]

aoc commands are:````
   run      Runs submissions
   create   Creates a new submission
   config   Configures user's parameters
```

### Examples

#### Run last problem

```
./aoc run
```

```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running submissions for day 04:

* part 2:
---------------------------------------------------
Avg over all inputs
---------------------------------------------------
----------  ----------  -----------  ---
jessy          78452        1.99 ms  py
maxime         43695        2.39 ms  py
----------  ----------  -----------  ---
```

#### Run specific problems from specific users

```
./aoc run -d 1 -d 2 -p 1 -a jessy -a maxime
```

```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running submissions for day 01:

* part 1:
---------------------------------------------------
Avg over all inputs
---------------------------------------------------
-----  -------  -----------  ---
jessy     543      0.46 ms   py
maxime    445      4.94 ms   cpp
-----  -------  -----------  ---
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running submissions for day 02:

* part 1:
---------------------------------------------------
Avg over all inputs
---------------------------------------------------
-----  --------  -----------  ---
jessy    5658      1.22 ms    py
maxime   6448      4.84 ms    cpp
-----  --------  -----------  ---
```

You can use `-r` to run each submission on its own input, or `-e` to print non-aggregated results.  
see `./aoc run -h` for full arguments description.

## Add your solution !

Create a new branch (e.g `[username]/day-[number]`)

For now we support `c`, `c++`, `java`, `javascript`, `typescript` , `go`, `python 3` (+ `cython`), `ruby`, `rust (stable)` and `bash` scripts.

You can use `./aoc create` tool to create a new empty submission:

```
usage: aoc create [-h] [-a AUTHOR] [-d DAY] [-p PART]
                  [-l {c,cpp,go,java,js,ts,py,pyx,rb,rs,sh}]

Create a new submission

optional arguments:
  -a AUTHOR, --author AUTHOR
                        submission author
  -d DAY, --day DAY     problem day
  -p PART, --part PART  problem part
  -l {c,cpp,go,java,js,ts,py,pyx,rb,rs,sh}, --language {c,cpp,go,java,js,ts,py,pyx,rb,rs,sh}
                        submission language
```
After which you can paste your puzzle input in `day-[number]/input/[username].txt` and write your code in `day-[number]/part-[number]/[username].py`.

you can also use `./aoc config` to setup your local profile

```
usage: aoc config [-h] username {c,cpp,go,java,js,ts,py,pyx,rb,rs,sh}

Configures user parameters

positional arguments:
  username              prefered username
  {c,cpp,go,java,js,ts,py,pyx,rb,rs,sh}
                        prefered programming language
```

### Additional info

You can add other functions & modules if you need to. Any external dependency should be added to `requirements.txt`.

Once you tested your solution you can submit it by making a PR.
