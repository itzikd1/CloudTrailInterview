# python developer task
Your task contains 3 parts:
1. Parse cloud data file into an object and create a simple security rule.
2. Use `cloudrai-knowledge` package to write and test a simple security rule.
3. Use `cloudrai-knowledge` package to write and test a security rule with logic.

### Part 1
Your task here is to update the code in [main.py](cloudrail/main.py). 
You will find 2 #TODO comments in it to complete.
#### 1.a Parse json into an object
Parse the file [ec2-describe-instances.json](cloudrail/cloud-data/ec2-describe-instances.json) into the object [ec2](cloudrail/entities/ec2.py).
#### 1.b find objects that have environment=production tag
write a logic in `get_ec2_contains_production_tag` function that finds ec2s that have environment=production tag.
```json
{
  "Tags": [
    {
      "Key": "environment",
      "Value": "production"
    }
  ]
}
```

### Part 2
Now write the exact same rule, but using `cloudrail-knowledge` python package. You can find documentation [here](https://knowledge.docs.cloudrail.app/).

### Part 3
Write a new rule that alerts (create an issue) if there are 2 (or more) ec2s with similar names.
A similar name is when there is one letter difference between 2 names.

For example:
* `cat` and `cab` are  similar
* `cat` and `dog` are not  similar
* `dog` and `god` are  not similar (same letter in different order do not consider as similar)
* `god` and `good` are  similar (only 1 missing letter)

---
**NOTES**

1. Make sure to run the unit tests under `tests` folder
2. Parts 2-3 should be done using the files under the `rules` folder.

---