In order:

- [x] Update requirements.txt
- [x] Write redis.conf
- [x] Re-write setup.md
- [x] Re-write /services files to use /opt
- [x] Refactor main.py to use Redis instead of fs.localData
- [x] Refactor backgroundTasks.py to use Redis instead of fs.localData
- [x] Re-write setup.py to use new service files (username not needed?)
- [x] Check if redis.conf file needs certain permissions
- [x] Re-write /tools
- [x] Work out why NGINX isn't connecting to infoWebServer
- [x] Deal with errors that can occur from Redis (e.g. losing connection)
- [ ] Send error embed when add/removechannel is called and Redis can't be connected to
- [ ] Make sure that `subscribedChannels` is fully returned from Redis
- [ ] Fix permission error for Redis logging

Not redis branch related:

- [ ] Don't show `r/SpaceX Discussion` line in information embed if there is no url
- [ ] Show in launch information notifications what has changed since the last notification
