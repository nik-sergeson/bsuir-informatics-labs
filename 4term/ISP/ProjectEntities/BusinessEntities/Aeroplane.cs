using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.ComponentModel;

public class Aeroplane:BuisnessEntity,INotifyPropertyChanged
{
    private int _id;
    private int _flightid;
    private int _capacity;

    public override int ID
    {
        get { return _id; }
        set { SetProperty(ref _id, value, "ID"); }
    }

    public int FlightID
    {
        get { return _flightid; }
        set { SetProperty(ref _flightid, value, "FlightID"); }
    }

    public int Capacity
    {
        get { return _capacity; }
        set { SetProperty(ref _capacity, value, "Capacity"); }
    }

    public Aeroplane(int id, int flightid, int capacity)
    {
        _id = id;
        _flightid = flightid;
        _capacity = capacity;
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