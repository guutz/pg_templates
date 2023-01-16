[b]Supported platforms for LLR tasks:[/b][list]
*Windows: 32 bit, 64 bit
*Linux: 32 bit, 64 bit
*Mac: 64 bit
*Multi-threading is supported and IS recommended. Click [url=https://www.primegrid.com/prefs_edit.php?subset=project#mt]here[/url] to set the maximum number of threads.
*Uses fast proof tasks so no double check tasks are needed. Everyone is "first"![/list]
Intel and recent AMD CPUs with FMA3 capabilities (Haswell or better for Intel, Zen-2 or better for AMD) will have a very large advantage running LLR tasks, and CPUs with AVX-512 capabilities (certain recent Intel Skylake-X and Xeon CPUs, AMD Ryzen 7000 and EPYC CPUs) will be the fastest.

Note that LLR is running the latest AVX-512 version of LLR which takes full advantage of the features of these newer CPUs. It's faster than the previous LLR app and draws more power and produces more heat, especially if they're highly overclocked. [color=orange][b]If you have certain recent Intel Skylake-X, Xeon, or AMD Zen-4+ CPUs, especially if it's overclocked or has overclocked memory, and haven't run the new AVX-512 LLR before, we strongly suggest running it before the challenge while you are monitoring the temperatures.[/b][/color]
