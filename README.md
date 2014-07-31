CFDG Optimizer: An optimization tool for improving CFDG grammar files.

CFDG grammar files are shape grammar files created for the [Context Free](http://contextfreeart.org/) program.

This tool will adjust the rule probabilities of CFDG grammars to produce output that most closely matches a 
list of example images that you provide.


Installing cfdg-optimizer
=========================

On Debian Linux:

```
sudo apt-get install gfortran libopenblas-dev liblapack-dev
pip install cfdg-optimizer
```

Now you should be able to use cfdg-optimizer using the `cfdgo` command.


Using cfdg-optimizer
====================

You must have:
* An existing CFDG grammar file
* A directory of images that you want your grammar to closely produce

Let's suppose the grammar file is called `grammar.cfdg` and the images directory is called `testimages/`.

1. Open your grammar file for editing.

2. Add a wildcard ('*') to every rule whose rule probability you want modified.  If the rule has a probability,
   this wildcard goes between the rule name and the probability value.  Otherwise, the wildcard should go after the 
   rule name.  For example:
    ```
    rule examplerule             --->  rule examplerule *
    rule anotherexamplerule 1.5  --->  rule anotherexamplerule * 1.5
    ```

3. Run the `cfdgo` command like so:
    
```bash
cfdgo grammar.cfdg /path/to/testimages/
```

4. cfdg-optimizer should calculate the optimal probabilities for the rules that you marked for modification. When
   done, it will return the optimial grammar variant in its own file.

   
   
