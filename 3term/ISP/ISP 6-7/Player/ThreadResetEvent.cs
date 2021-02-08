using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;

public class ThreadResetEvent
{
    public Thread curthread { get; set; }
    public ManualResetEvent MRE { get; set; }
}