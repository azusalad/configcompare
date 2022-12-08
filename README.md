# configcompare
Compares two configs for Valve Source games.
For example if your two input configs are:

`// Example Autoexec 1
unbindall
bind "0" "slot10"

fov_desired 90
mat_phong "0"
sv_cheats 1
sv_pure 0 // comment
// another comment`
 
 and 
 
`// Example Autoexec 2
unbindall
bind "0" "slot10"
mat_specular 1

sv_cheats 0
sv_pure 1
// comment
cl_interp 0 // another comment`

Then the output would be

`// ----------------------------------------------------------------------------
// exampleautoexec1.cfg only
// ----------------------------------------------------------------------------
fov_desired "90"
mat_phong "0"

// ----------------------------------------------------------------------------
// exampleautoexec2.cfg only
// ----------------------------------------------------------------------------
mat_specular "1"
cl_interp "0"

// ----------------------------------------------------------------------------
// In both files but different values.
// ----------------------------------------------------------------------------

// Quick compare list.  Format: command "{f1_name}" "{f2_name}"
sv_cheats "1" "0"
sv_pure "0" "1"


// Taking values from exampleautoexec1.cfg
sv_cheats "1"
sv_pure "0"


// Taking values from exampleautoexec2.cfg
sv_cheats "0"
sv_pure "1"
`

## Usage

Edit config.py first with the locations of the config files you want to compare, and words to ignore.  Then run the program.

`python main.py`
