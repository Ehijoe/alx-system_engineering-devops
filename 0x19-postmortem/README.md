# Update Issue Postmortem

This is the postmortem for the downtime of the ALX Whaha website that occurred
on the 21st of February, 2023.

## Issue Summary

From 9:00 am to 10:25 am WAT on the 21st of February, 2023, the ALX Whaha
website experienced downtime after an update of the software from version 1.0 to
1.1. All users who tried to access the site during this time got a 404 error.
The root cause was a failure to update the server configuration during the
update.

## Timeline (West African Time)

- 9:00 am - Servers are updated and service stops working.

- 9:12 am - Customers complain that the site is unreachable.

- 9:42 am - Dev team is called in to investigate issue.

- 10:15 am - Server configuration is updated and tested.

- 10:25 am - Servers are fully online and functional.

## Root Cause

The servers were updated at 9:00am with the help of an update script. The update
script however did not handle the configuration of nginx to proxy requests to
the application server. This caused nginx to give a 404 error when any request
was made.

![nginx 404 error](https://www.linuxbabe.com/wp-content/uploads/2021/06/nginx-404-not-found.webp "Nginx 404 Error")

## Resolution

## Corrective and preventative measures
