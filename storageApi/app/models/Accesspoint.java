package models;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

import org.codehaus.jackson.node.ObjectNode;

import play.data.validation.Constraints;
import play.db.ebean.Model;
import play.libs.Json;

@Entity
public class Accesspoint extends Model {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    public Long apId;
    @Constraints.Required
    public String ssid;
    @Constraints.Required
    public String mac;
    @Constraints.Required
    public String encrypted;

    public static Finder<Long, Accesspoint> find = new Finder<Long, Accesspoint>(Long.class,
            Accesspoint.class);

    public Accesspoint(String ssid, String mac, String encrypted) {
        super();
        this.ssid = ssid;
        this.mac = mac;
        this.encrypted = encrypted;
    }

    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder();
        builder.append("Committer [ssid=");
        builder.append(ssid);
        builder.append(", encrypted=" + encrypted);
        builder.append(", mac=");
        builder.append(mac + "]");
        return builder.toString();
    }

    public ObjectNode toObjectNode() {
        ObjectNode result = Json.newObject();
        result.put("ssid", ssid);
        result.put("mac", mac);
        result.put("encrypted", encrypted);
        return result;
    }
}
