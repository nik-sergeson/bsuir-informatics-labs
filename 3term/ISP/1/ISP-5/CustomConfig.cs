using System;
using System.Configuration;

public class CustomConfig : ConfigurationSection
{
    [ConfigurationProperty("pathinfo",IsRequired=true)]
    public Element Pathinfo
    {
        get { return (Element)base["pathinfo"]; }
    }
}

public class Element : ConfigurationElement
{
    [ConfigurationProperty("path", IsRequired = true)]
    public string Path
    {
        get { return (string)base["path"]; }
        set { base["path"] = value; }
    }
}