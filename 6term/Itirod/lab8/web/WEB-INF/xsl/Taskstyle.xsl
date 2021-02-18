<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	 
    <xsl:template match="/">
        <html>
            <body>
                <h1>Task details</h1>
                <table border="1">
                    <tr>
                        <th>ID</th>
                        <th>description</th>
                        <th>User id</th>
                        <th>opendate</th>
                        <th>deadline</th>
                        <th>priority</th>
                    </tr>
                    <xsl:for-each select="list/com.lab5.model.Task">
                        <tr>
                            <td>
                                <xsl:value-of select="ID"/>
                            </td>
                            <td>
                                <xsl:value-of select="description"/>
                            </td>
                            <td>
                                <xsl:value-of select="user/ID"/>
                            </td>
                            <td>
                                <xsl:value-of select="opendate"/>
                            </td>
                            <td>
                                <xsl:value-of select="deadline"/>
                            </td>
                            <td>
                                <xsl:value-of select="priority"/>
                            </td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet> 