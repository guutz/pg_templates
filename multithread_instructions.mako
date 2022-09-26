<%page args="mt" expression_filter="h"/>\
* Your mileage may vary. [b][u]Before[/u][/b] the challenge starts, take some time and experiment and see what works best on [b]your[/b] computer.
* If you have a CPU with hyperthreading or SMT, either turn off this feature in the BIOS, or set BOINC to use 50% of the processors.[list]
*If you're using a GPU for other tasks, it may be beneficial to leave hyperthreading on in the BIOS and instead tell BOINC to use 50% of the CPU's. This will allow one of the hyperthreads to service the GPU.[/list]
% if mt != 'yes_app':
* [u][b]The new multi-threading system is now live. Click [url=https://www.primegrid.com/prefs_edit.php?venue=home&subset=project&cols=1&tnow=1595298865&ttok=78887263307c0cc2e93f633c9a9953d4#mt]here[/url] to set the maximum number of threads.[/b][/u] This will allow you to select multi-threading from the project preferences web page. No more app_config.xml. It works like this:[list]
* In the preferences selection, there are selections for "max jobs" and "max cpus", similar to the settings in app_config.
* Unlike app_config, these two settings apply to ALL apps. You can't chose 1 thread for SGS and 4 for SoB. When you change apps, you need to change your multithreading settings if you want to run a different number of threads.
* There will be individual settings for each venue (location).
* This will eliminate the problem of BOINC downloading 1 task for every core.
* The hyperthreading control isn't possible at this time.
* The "max cpus" control will only apply to LLR apps. The "max jobs" control applies to all apps.[/list]
* If you want to continue to use app_config.xml for LLR tasks, you need to change it if you want it to work. Please see [url=https://www.primegrid.com/forum_thread.php?id=8750&nowrap=true#132260]this message[/url] for more information.
* Some people have observed that when using multithreaded LLR, hyperthreading is actually beneficial. We encourage you to experiment and see what works best for you.[/list]
% else:
*[u]Use GFN's multithreaded mode. It requires a little bit of setup, but it's worth the effort. Follow these steps:[/u]
[list]
*Create a app_config.xml file in the directory C:\ProgramData\BOINC\projects\www.primegrid.com\ (or wherever your BOINC data directory is located). For a quad core CPU, the file should contain the following contents. Change the two occurrences of "4" to the number of actual cores your computer has.

[pre]<app_config>
   <app_version>
       <app_name>genefer</app_name>
       <cmdline>-nt 4</cmdline>
       <plan_class>cpuGFN21</plan_class>
       <avg_ncpus>4</avg_ncpus>
   </app_version>
</app_config>[/pre]

*After creating the file, click on "Options/Read config files". You should then restart BOINC or reboot.
*The first time BOINC downloads a GFN task, it may act a little strange and download 4 tasks instead of 1. The run times on this first set of tasks may look a bit strange too. This is normal. This will also occur anytime BOINC downloads more than one task at a time. This can be avoided by setting "Use at most [ 1 ] % of the CPUs" before you download GFN tasks. After one task was downloaded, increase the percentage.
*Some people have observed that when using multithreaded GFN, hyperthreading is actually beneficial. We encourage you to experiment and see what works best for you.
[/list]
% endif
