using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.ComponentModel;

    public class Passport:BuisnessEntity, INotifyPropertyChanged
    {
        private int _personid;
        private string _address;
        private string _photo;
        private string _name;
        private string _secondname;

        public override int ID
        {
            get { return _personid; }
            set { SetProperty(ref _personid, value, "ID"); }
        }

        public string Address
        {
            get { return _address; }
            set
            {
                SetProperty(ref _address, value, "Address");
            }
        }

        public string Photo
        {
            get { return _photo; }
            set { SetProperty(ref _photo, value, "Photo"); }
        }

        public string Name
        {
            get { return _name; }
            set { SetProperty(ref _name, value, "Name"); }
        }

        public string SecondName
        {
            get { return _secondname; }
            set { SetProperty(ref _secondname, value, "SecondName"); }
        }

        public Passport()
        {
            _personid = -1;
            _address = "Noaddress";
            _photo = "Nophoto";
            _name = "Noname";
            _secondname = "Noname";
        }

        public Passport(int pesonid, string address, string photo, string name, string secondname)
        {
            _personid = pesonid;
            _address = address;
            _photo = photo;
            _name = name;
            _secondname = secondname;
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