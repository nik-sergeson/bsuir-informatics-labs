using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;

namespace MyTowerDefence
{
    public class StaticTower:StaticSprite
    {
        protected int _attackradius;
        protected int _bullattackradius;
        protected int _bulldamage;
        protected int _bullmaxspeed;
        protected BuildingType _towertype;
        protected int _cost;
        protected Texture2D _outtexture;

        public int attackradius
        {
            get { return _attackradius; }
            private set { _attackradius = value; }
        }

        public int bullattackradius
        {
            get { return _bullattackradius; }
            private set { _bullattackradius = value; }
        }

        public int bulldamage
        {
            get { return _bulldamage; }
            private set { _bulldamage = value; }
        }

        public int bullmaxspeed
        {
            get { return _bullmaxspeed; }
            private set { _bullmaxspeed = value; }
        }

        public int cost
        {
            get { return _cost; }
            private set { _cost = value; }
        }

        public Texture2D outtexture
        {
            get { return _outtexture; }
            set { _outtexture = value; }
        }

        public BuildingType towertype
        {
            get { return _towertype; }
            set { _towertype = value; }
        }

        public StaticTower(Texture2D textureImage, Vector2 position, float layerdepth,Texture2D outtexture,BuildingType towertype):base(textureImage,position,layerdepth)
        {
            _outtexture = outtexture;
            if (towertype == BuildingType.AntiAerienne)
            {
                _attackradius = 90;
                _bullattackradius = 190;
                _bulldamage = 20;
                _bullmaxspeed = 5;
                _towertype = BuildingType.AntiAerienne;
                _cost = 10;
            }
            else if (towertype == BuildingType.Archer)
            {
                _attackradius = 100;
                _bullattackradius = 200;
                _bulldamage = 30;
                _bullmaxspeed = 6;
                _towertype = BuildingType.Archer;
                _cost = 20;
            }
            else
            {
                _attackradius = 110;
                _bullattackradius = 210;
                _bulldamage = 40;
                _bullmaxspeed = 7;
                _towertype = BuildingType.DeFeu;
                _cost = 30;

            }
        }
    }
}
