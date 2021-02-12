using System;
using FileSavers;

namespace FactoryFileSavers
{
    public abstract class SaveManager
    {
        public abstract IDocStorage Create();
    }
}