# url-check

A Python script to check if a CSV of URLs is accessible

> [!WARNING]
>
> This is a work in progress, things may be broken or unstable!

## Formatting CSV

The formatting for a CSV goes as follows:

```csv
URL,Note,Blocked by,Reason
```

`Note` and `Reason` can be different, but the placement of those two columns must be placed correctly.

## How to run

1. Populate CSV
2. Place CSV in the same directory as the script
3. Run `checkWhitelist.py`
4. Wait until completed
