# PyLogger - Just another Keylogger...
#### A basic try to create a KeyLogger with Python and data exfiltration using a WebHook from Discord

#### REQUIREMENTS
```python3 -m pip install keyboard ```

#### USAGE
**Discord:**
You will need to create a webhook in a Discord channel.
`Edit Channel > Integrations > New webhook`
Copy and paste the webhook URL in the python code `main.py`
**File:**
Change `REPORT_METH = "discord"` to `REPORT_METH = "file"`
The logs will be created in the same directory of execution.

If you want to change the exfiltration time change it (seconds).

*NOTE: This is a fast just try CAPITAL LETTERS may fail because on start figure that CAPS LOCK is OFF.*