using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.ComponentModel;

public class Baggage:BuisnessEntity,INotifyPropertyChanged
{
    private int _weight;
    private int _ownerid;

    public int Weight
    {
        get { return _weight; }
        set { SetProperty(ref _weight, value, "Weight"); }
    }

    public override int ID
    {
        get { return _ownerid; }
        set { SetProperty(ref _ownerid, value, "ID"); }
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

    public Baggage()
    {
        _ownerid = -1;
        _weight = 0;
    }

    public Baggage(int ownerid, int weight)
    {
        _ownerid = ownerid;
        _weight = weight;
    }
}
