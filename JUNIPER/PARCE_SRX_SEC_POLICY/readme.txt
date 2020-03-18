Before parce prepare file with policy config. Take it from output of command:
admin@srx# show security policies

If you have default policy & policy rematch like this:

default-policy {
    deny-all;
}
policy-rematch;


Delete this from file with config which you want parce 
