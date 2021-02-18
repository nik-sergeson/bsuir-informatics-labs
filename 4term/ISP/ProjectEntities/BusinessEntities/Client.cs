using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.ComponentModel;

public class Client:BuisnessEntity, INotifyPropertyChanged
{
    private int _id;
    private string _name;

    public override int ID
    {
        get { return _id; }
        set { SetProperty(ref _id, value, "ID"); }
    }

    public string Name
    {
        get { return _name; }
        set { SetProperty(ref _name, value, "Name"); }
    }

    public Client()
    {
        _id = -1;
        _name = "Noname";
    }

    public Client(string name,int id)
    {
        _id = id;
        _name = name;
    }

    public event PropertyChangedEventHandler PropertyChanged;
    private void SetProperty<T>(ref T field, T value, string name)
    {
        if (!EqualityComparer<T>.Default.Equals(field, value))
        {
            field = value;
            var handler = PropertyChanged;
            if (handler != null)
            {
                handler(this, new PropertyChangedEventArgs(name));
            }
        }
    }
}
