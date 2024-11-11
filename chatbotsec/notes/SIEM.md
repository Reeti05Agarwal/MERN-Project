SIEM
# SIEM


## Important
1. Collect Data
2. Aggregated Data
3. Discover and Detect Threats
4. Identify Breaches and Investigate Alerts 


### Linux Workstation

Linux OS stores all the related logs, such as events, errors, warnings, etc. Which are then ingested into SIEM for continuous monitoring. Some of the common locations where Linux store logs are:

    /var/log/httpd : Contains HTTP Request  / Response and error logs.
    /var/log/cron   : Events related to cron jobs are stored in this location.
    /var/log/auth.log and /var/log/secure : Stores authentication related logs.
    /var/log/kern : This file stores kernel related events.
