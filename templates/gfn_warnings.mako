<%page args="sp_list"/>\
[b]Supported platforms for GFN tasks:[/b][list]
*Windows: CPU¹: x86, x64. GPU²: Nvidia, AMD, Intel ARC.
*Linux: CPU¹: x86, x64, ARM64. GPU²: Nvidia, AMD, Intel ARC.
*Mac: CPU¹: x64, ARM64. GPU2: Nvidia, AMD, Apple M-Series.
*For CPU tasks, multi-threading is supported and IS recommended. Click [url=https://www.primegrid.com/prefs_edit.php?subset=project#mt]here[/url] to set the maximum number of threads.
*For GFN-21 CPU and GFN-22 CPU tasks, multi-threading is turned on automatically. A minimum of 4 CPU logical cores are required.
*Except for GFN-15, all GFN use fast proof tasks so no double check tasks are needed. Everyone is "first"!

¹ CPU tasks are not available for GFN-15 (n=32768) or "Do You Feel Lucky?".
² OpenCL 1.1 or higher is required.[/list]
% for sp in sp_list:
% if 'GFN' in sp.short_name:
${sp.short_name} WU's are currently averaging \
% if sp.cpu_time:
${sp.cpu_time} on CPU and \
% endif
${sp.gpu_time} on GPU.
For a general idea of how your GPU stacks up, you can have a look at the [url=http://www.primegrid.com/gpu_list.php]fastest GPUs list[/url].
% endif
% endfor