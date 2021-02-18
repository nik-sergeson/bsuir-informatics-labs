using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;

namespace MyTowerDefence
{
    [Serializable]
    public class Enemy:Sprite
    {
        public override Vector2 direction
        {
            get { return speed; }
        }
        private List<Vector2> road;
        private int checkpoint;
        protected int healthpoints;
        protected float maxspeed;
        protected int fullhealth;
        private float angle;
        protected string texturepath;
        [NonSerialized]
        private Texture2D healthrow;
        public int cost { get; set; }

        public int HealthPoint
        {
            get { return healthpoints; }
            set { healthpoints = value; }
        }

        public bool AtFinishPoint
        {
            get { return ((Math.Abs(road[road.Count-1].X - position.X) <= textureImage.Width/2) &&(Math.Abs(road[road.Count-1].Y - position.Y) <= textureImage.Height/2)); }
        }

        public override void Update(GameTime gameTime)
        {
            position += direction;
            if (checkpoint < road.Count - 1)
            {
                if (((Math.Abs(road[checkpoint].X - position.X) <= Math.Abs(speed.X / 2)) && (speed.X != 0)) || ((Math.Abs(road[checkpoint].Y - position.Y) <= Math.Abs(speed.Y / 2)) && (speed.Y != 0)))
                {
                    ++checkpoint;
                    double r=Math.Sqrt(Math.Pow(road[checkpoint].X - road[checkpoint - 1].X,2.0)+Math.Pow(road[checkpoint].Y - road[checkpoint - 1].Y,2.0));
                    speed.X = (float)(maxspeed * ((road[checkpoint].X - road[checkpoint - 1].X)/r));
                    speed.Y = (float)(maxspeed *((road[checkpoint].Y - road[checkpoint - 1].Y)/r));
                    angle = (float)(Math.Atan2(speed.Y,speed.X)-Math.PI/2);
                }
            }
            base.Update(gameTime);
        }

        public Vector2 FuturePosition(int redrawcount)
        {
            Vector2 futurespeed = new Vector2 { X = speed.X, Y = speed.Y };
            float maxspeed = Math.Abs((futurespeed.X == 0) ? futurespeed.Y : futurespeed.X);
            double time = 0, tbetwinchp;
            int futurechekpoint = checkpoint;
            tbetwinchp = ((speed.X == 0) ? 0 : (Math.Abs(position.X - road[checkpoint].X) / Math.Abs(speed.X))) + ((speed.Y == 0) ? 0 : (Math.Abs(position.Y - road[checkpoint].Y) / Math.Abs(speed.Y)));
            if (tbetwinchp > redrawcount)
                return new Vector2(position.X + speed.X * redrawcount, position.Y + speed.Y * redrawcount);
            else
                time += tbetwinchp;
            while (true)
            {
                futurechekpoint++;
                if (futurechekpoint == road.Count)
                    return road[road.Count - 1];
                futurespeed.X = maxspeed * Math.Sign(road[futurechekpoint].X - road[futurechekpoint - 1].X);
                futurespeed.Y = maxspeed * Math.Sign(road[futurechekpoint].Y - road[futurechekpoint - 1].Y);
                tbetwinchp = ((futurespeed.X == 0) ? 0 : (Math.Abs(road[futurechekpoint - 1].X - road[futurechekpoint].X) / Math.Abs(futurespeed.X))) + ((futurespeed.Y == 0) ? 0 : (Math.Abs(road[futurechekpoint - 1].Y - road[futurechekpoint].Y) / Math.Abs(futurespeed.Y)));
                if (redrawcount - time <= tbetwinchp)
                    return new Vector2((float)(road[futurechekpoint - 1].X + futurespeed.X * (redrawcount - time)), (float)(road[futurechekpoint - 1].Y + futurespeed.Y * (redrawcount - time)));
                else
                    time += tbetwinchp;
            }
        }

        public List<Vector2> FutureCheckpoints(int attackradius,float x,float y)
        {
            List<Vector2> futpoint = new List<Vector2>();
            Vector2 futurespeed = new Vector2 (Math.Sign(speed.X), Math.Sign(speed.Y)),nextpos=new Vector2(position.X,position.Y);
            int futurechekpoint = checkpoint;
            while(true)
            {
                nextpos.X = nextpos.X + collisionRect.Width * futurespeed.X;
                nextpos.Y = nextpos.Y + collisionRect.Height * futurespeed.Y;
                if (Math.Pow(x - nextpos.X, 2.0) + Math.Pow(y - nextpos.Y, 2.0) > Math.Pow(attackradius, 2.0))
                    break;
                if (((Math.Abs(road[futurechekpoint].X - nextpos.X) <= Math.Abs(collisionRect.Width/2)) && (futurespeed.X != 0)) || ((Math.Abs(road[futurechekpoint].Y - nextpos.Y) <= Math.Abs(collisionRect.Height/2)) && (futurespeed.Y != 0)))
                {
                    futurechekpoint++;
                    if (futurechekpoint == road.Count)
                        break;
                    futurespeed.X = Math.Sign(road[futurechekpoint].X - road[futurechekpoint - 1].X);
                    futurespeed.Y = Math.Sign(road[futurechekpoint].Y - road[futurechekpoint - 1].Y);
                }
                futpoint.Add(new Vector2(nextpos.X, nextpos.Y));
            }
            return futpoint;
        }

        public override void Draw(SpriteBatch spriteBatch)
        {         
            spriteBatch.Draw(textureImage, position, null, Color.White, angle, new Vector2(textureImage.Width/2,textureImage.Height/2), 1, SpriteEffects.None, (float)0.1);
            spriteBatch.Draw(healthrow, new Rectangle(this.collisionRect.X-(int)(this.collisionRect.Width/2),this.collisionRect.Y-this.collisionRect.Height/2-5,this.collisionRect.Width,5),null, Color.Black,0,Vector2.Zero,SpriteEffects.None,(float)0.01);
            spriteBatch.Draw(healthrow, new Rectangle(this.collisionRect.X - (int)(this.collisionRect.Width / 2), this.collisionRect.Y - this.collisionRect.Height / 2-5, (int)(this.collisionRect.Width * ((double)HealthPoint / (double)fullhealth)), 5), null, Color.Red, 0, Vector2.Zero, SpriteEffects.None, 0);
        }

        public Enemy(Texture2D textureImage,GraphicsDevice gdevice, Vector2 position, float speed,float layerdepth,List<Vector2> road,string texturepath): base(textureImage, position, new Vector2(0,speed),layerdepth)
        {
            this.road = new List<Vector2>(road);
            this.maxspeed = speed;
            checkpoint = 1;
            this.texturepath = texturepath;
            healthrow = new Texture2D(gdevice, 1, 1);
            healthrow.SetData(new[] { Color.White });
        }

        public void UpdateTexture(Game game,GraphicsDevice gdevice)
        {
            textureImage = game.Content.Load<Texture2D>(texturepath);
            healthrow = new Texture2D(gdevice, 1, 1);
            healthrow.SetData(new[] { Color.White });
        }
    }
}
