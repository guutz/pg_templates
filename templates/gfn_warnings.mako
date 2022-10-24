<%page args="cpu_time,gpu_time,short_name"/>\
[u][b]Application Builds[/b][/u]

[list][color=red][b]IMPORTANT: Overclocking -- including factory overclocking -- on Nvidia GPUs [u]is very strongly discouraged[/u]. Even if your GPU can run other tasks without difficulty, it may be unable to run GFN tasks when overclocked.[/b][/color]

Supported platforms:
*Windows: Nvidia GPU (OpenCL): 32 bit, AMD/ATI GPU (OpenCL): 32 bit${', CPU: 64 bit, 32 bit' if cpu_time else ''}
*Linux: Nvidia GPU (OpenCL): 32 bit, 64 bit, AMD/ATI GPU (OpenCL): 32 bit, 64 bit${', CPU: 64 bit, 32 bit' if cpu_time else ''}
*Mac: Nvidia GPU (OpenCL): 64 bit, AMD/ATI GPU (OpenCL): 64 bit${', CPU: 64 bit, 32 bit' if cpu_time else ''}
[/list]


[u][b]A Cautionary Reminder[/b][/u]

[list][color=red][b]ATTENTION: The primality programs Genefer (for CPUs) and GeneferOCL (for GPUs) are computationally intensive; so, it is vital to have a stable system with good cooling. It does not tolerate "even the slightest of errors." Please see [url=http://www.primegrid.com/forum_thread.php?id=857&nowrap=true#8317]this post[/url] for more details on how you can "stress test" your CPU, and please see [url=http://www.primegrid.com/forum_thread.php?id=4148]this post[/url] for tips on running GFN on your GPU successfully.

[u]As with all number crunching, excessive heat can potentially cause permanent hardware failure. Please ensure your cooling system is sufficient.[/u]

${short_name} WU's are currently averaging \
% if cpu_time:
${cpu_time} on CPU and \
% endif
${gpu_time} on GPU.
For a general idea of how your GPU stacks up, you can have a look at the [url=http://www.primegrid.com/gpu_list.php]fastest GPUs list[/url].

If your CPU is highly overclocked, please consider "stress testing" it. Overclocking your GPU is not recommended at all for GeneferCUDA. Sieving is an excellent alternative for computers that are not able to run Genefer. :)

Please, please, please make sure your machines are up to the task.[/b][/color]
[/list]
