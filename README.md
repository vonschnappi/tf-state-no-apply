# Get terraform .tfstate without running apply

## Why I created this repo
I was struggilng with generating a .tfstate file without running the `terraform apply` command. 
You could run plan but that generates a binary that you can't use later if you want to run `terraform destroy`.
You could create the plan with `-destory` flag but that would only create it as a destroy plan.

In short, I need a .tfstate.

## How I solved it
There was nothing online, surprisingly enough, on how to do it. Nor were there any other devs looking to do the same thing. 
So I created a small shell script coupled with a small python script.

What they do:
* Create an empty .tfstate file
* Create a plan, get its output and cat a to temp json file
* From the temp json file, get the resources part and append it to the empty .tfstate file

That's it.

## Prerequisites 
You need to [install jq](https://stedolan.github.io/jq/download/) on the machine that runs terraform.

## Running
1. Put both shell and pythong script in the folder that contains all of your .tf files.
2. Run 
