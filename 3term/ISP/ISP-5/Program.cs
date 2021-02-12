using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Configuration;
using System.Reflection;
using System.IO;
using Solver;

namespace ISP_5
{
    class Program
    {
        static void Main(string[] args)
        {
            IEnumerable<string> files;
            string command=" ";
            string name = ConfigurationManager.AppSettings["filepath"];
            var watcher = new FileSystemWatcher
            {
                Path = name,
                Filter = "*.dll"
            };
            FileSystemEventHandler handler = (o, e) =>
            {
                Console.Clear();
                files = Directory.EnumerateFiles(name, "*.dll");
                foreach (var str in files)
                {
                    Console.WriteLine(str);
                }
            };
            watcher.Created += handler;
            watcher.Deleted += handler;
            watcher.EnableRaisingEvents = true;
            files = Directory.EnumerateFiles(name, "*.dll");
            foreach (var str in files)
            {
                Console.WriteLine(str);
            }
            while (command.Length != 0)
            {
               Console.WriteLine("Choose plugin");
                command = Console.ReadLine();
                foreach (string plug in files)
                {
                    if (plug.Contains(command))
                    {
                        AssemblyName aname = AssemblyName.GetAssemblyName(plug);
                        Assembly asemb = Assembly.Load(aname);
                        Type[] types = asemb.GetTypes();
                        foreach(Type type in types)
                        {
                            try
                            {
                                var solv = (ISolver)Activator.CreateInstance(type);
                                Console.WriteLine(solv.ShuntingYard("e(4+3)*7"));
                            }
                            catch (Exception)
                            {
                              
                            }
                        }
                        break;
                    }
                }
            }
            watcher.Dispose();
        }
    }
}
