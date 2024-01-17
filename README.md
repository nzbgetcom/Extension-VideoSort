> **Note:** this repo is a fork of the original github [project](https://github.com/nzbget/VideoSort)
> made by @hugbug.

## NZBGet Versions

- pre-release v23+  [v10.0](https://github.com/nzbgetcom/Extension-VideoSort/releases/tag/v10.0)
- stable  v22 [v9.0](https://github.com/nzbgetcom/Extension-VideoSort/releases/tag/v9.0)
- legacy  v21 [v9.0](https://github.com/nzbgetcom/Extension-VideoSort/releases/tag/v9.0)

> **Note:** this script works with Python 3.8.x and above versions.
If you need Python 3.7.x and below support please use [v8.1](https://github.com/nzbgetcom/Extension-VideoSort/releases/tag/v8.1) release.
For Python 2.x support please use [v8](https://github.com/nzbgetcom/Extension-VideoSort/releases/tag/v8.0) release.

# VideoSort
[Post-processing](https://nzbget.com/documentation/post-processing-scripts/) script for [NZBGet](https://nzbget.com).

This is a script for downloaded TV shows and movies. It uses scene-standard naming conventions to match TV shows and movies and rename/move/sort/organize them as you like.

## Example

Let's say the download folder has following files:

    [dir]	/home/user/downloads/Futurama.S07E18.The.Inhuman.Torch.XVID
    [file]	/home/user/downloads/Futurama.S07E18.The.Inhuman.Torch.XVID/F0718TIT.avi

VideoSort can rename the video-file and move it into another directory creating sub-directories when necessary:

    [dir]	/home/user/videos/Futurama
    [dir]	/home/user/videos/Futurama/Season 7
    [file]	/home/user/videos/Futurama/Season 7/Futurama - S07E18 - The Inhuman Torch.avi

The formatting rules for destination file name (and sub-directories) are definable via configuration options.

VideoSort can organize:
 - seasoned tv shows;
 - dated tv shows;
 - movies.

## Installation

 - Download the newest version from [releases page](https://github.com/nzbgetcom/Extension-VideoSort/releases).
 - Unpack into pp-scripts directory. Your pp-scripts directory now should have folder "videosort" with subfolder "lib" and file "VideoSort.py";
 - Open settings tab in NZBGet web-interface and define settings for VideoSort;
 - Save changes and restart NZBGet.

## Formatting string

### Movies

 - %t, %.t, %_t - movie title with words separated with spaces, dots or underscores (case-adjusted);
 - %tT, %t.T, %t_T - movie title (original letter case);
 - %y	- year;
 - %decade - two-digits decade (90, 00, 10);
 - %0decade - four-digits decade (1990, 2000, 2010);
 - %imdb - IMDb ID, requires DNZB-header "X-DNZB-MoreInfo", containing link to imdb.com;
 - %cpimdb - IMDb ID (formatted for CouchPotato), requires DNZB-header "X-DNZB-MoreInfo", containing link to imdb.com.
 
### Seasoned TV shows

 - %sn, %s.n, %s_n - show name with words separated with spaces, dots or underscores (case-adjusted);
 - %sN, %s.N, %s_N - show name (original letter case);
 - %s - season number (1, 2);
 - %0s - two-digits season number (01, 02);
 - %e - episode number (1, 2);
 - %0e - two-digits episode number (01, 02);
 - %en, %e.n, %e_n - episode name (case-adjusted);
 - %eN, %e.N, %e_N - episode name (original letter case);

### Dated TV shows

 - %sn, %s.n, %s_n - show name with words separated with spaces, dots or underscores (case-adjusted);
 - %sN, %s.N, %s_N - show name (original letter case);
 - %y	- year;
 - %decade - two-digits decade (90, 00, 10);
 - %0decade - four-digits decade (1990, 2000, 2010).
 - %m	- month (1-12);
 - %0m	- two-digits month (01-12);
 - %d	- day (1-31);
 - %0d	- two-digits day (01-31);

### General

These specifiers can be used with all three types of supported video files:

 - %dn - original directory name (nzb-name);
 - %fn - original filename;
 - %ext - file extension;
 - %Ext - file extension (case-adjusted);
 - %qf - video format (HTDV, BluRay, WEB-DL);
 - %qss - screen size (720p, 1080i);
 - %qvc - video codec (x264);
 - %qac - audio codec (DTS);
 - %qah - audio channels (5.1);
 - %qrg - release group;
 - %cat - to refer to category ("%.cat", etc.);
 - %up - to navigate to parent directory;
 - {{text}} - uppercase the text;
 - {TEXT} - lowercase the text;

Credits
-------
The script relies on python libraries:

- [GuessIt 3.7.1](http://guessit.readthedocs.org) to extract information from file names and includes portions of code from [SABnzbd](https://sabnzbd.org/).
- [BabelFish 0.6.0](https://github.com/Diaoul/babelfish)
- [ReBulk 3.2.0](https://github.com/Toilal/rebulk/)
- [dateutil 2.8.2](https://github.com/dateutil/dateutil)
- [Six 1.16](https://github.com/benjaminp/six)
- [zipp 3.17](https://github.com/jaraco/zipp)
- [importlib_resources 6.1.1](https://github.com/python/importlib_resources)
