package controllers;

import java.util.ArrayList;
import java.util.List;

import models.Accesspoint;

import org.codehaus.jackson.JsonNode;
import org.codehaus.jackson.node.ObjectNode;

import play.libs.Json;
import play.mvc.Controller;
import play.mvc.Result;
import views.html.index;

public class Application extends Controller {

    public static Result index() {
        return ok(index.render("Your new application is ready."));
    }

    public static Result storeAp() {
        JsonNode json = request().body().asJson();
        String ssid = json.path("ssid").getTextValue();
        String mac = json.path("mac").getTextValue();
        String encrypted = json.path("encrypted").getTextValue();
        Accesspoint ap = new Accesspoint(ssid, mac, encrypted);
        ap.save();
        return ok();

    }

    public static Result getStoredAps() {
        List<Accesspoint> aps = Accesspoint.find.all();
        List<ObjectNode> jsonList = new ArrayList<ObjectNode>();
        for (Accesspoint ap : aps) {
            jsonList.add(ap.toObjectNode());
        }
        return ok(Json.toJson(jsonList.toArray()));
    }

}